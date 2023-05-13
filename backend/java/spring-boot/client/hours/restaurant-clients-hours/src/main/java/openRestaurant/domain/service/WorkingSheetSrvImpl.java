package openRestaurant.domain.service;

import org.apache.commons.lang3.tuple.Pair;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.DayOfWeek;
import java.time.LocalTime;
import java.util.*;
import java.util.regex.MatchResult;
import java.util.regex.Pattern;

@Service
public class WorkingSheetSrvImpl implements WorkingSheetSrv {
    private static final Logger LOGGER = LoggerFactory.getLogger(WorkingSheetSrvImpl.class);

    private final WorkingDaysSrv workingDaysSrv;

    private final WorkingHoursSrv workingHoursSrv;

    public WorkingSheetSrvImpl(@Autowired WorkingDaysSrv workingDaysSrv, @Autowired WorkingHoursSrv workingHoursSrv) {
        this.workingDaysSrv = workingDaysSrv;
        this.workingHoursSrv = workingHoursSrv;
    }

    @Override
    public Map<DayOfWeek, Set<Pair<LocalTime, LocalTime>>> workingSheetLineParser(String workingSheetStr) {
        //ex:"Mon-Mon, Sun 11:30 am - 10 pm ";
        LOGGER.info("parsing: {}", workingSheetStr);
        Objects.requireNonNull(workingSheetStr);
        final var workingSheetTerm = workingSheetStr.trim();
        var daysSheet = Pattern.compile(DAYS_PATTERN)
                .matcher(workingSheetTerm).results()
                .map(MatchResult::group)
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException(String.format("invalid input format. %s", workingSheetTerm)));
        String hoursSheet = workingSheetTerm.replace(daysSheet, "");
        var rawData = new HashMap<DayOfWeek, Set<Pair<LocalTime, LocalTime>>>();
        workingDaysSrv.parseWorkingDaysSheet(daysSheet)
                .stream()
                .map(d -> workingHoursSrv.calcWorkingHours(d, hoursSheet))
                .forEach(m -> {
                    m.forEach((k, v) -> {
                        if (rawData.containsKey(k)) {
                            rawData.put(k, new HashSet<>() {{
                                addAll(rawData.get(k));
                                addAll(v);
                            }});
                        } else {
                            rawData.put(k, v);
                        }
                    });
                });
        return rawData;
    }

    @Override
    public Map<DayOfWeek, Set<Pair<LocalTime, LocalTime>>> parseWorkingSheet(String workingSheetStr) {
        //ex:"Mon-Thu 11 am - 10:30 pm  / Fri 11 am - 11 pm  / Sat 11:30 am - 11 pm  / Sun 4:30 pm - 10:30 pm";
        LOGGER.info("parsing: {}", workingSheetStr);
        Objects.requireNonNull(workingSheetStr);
        return Arrays.stream(workingSheetStr.split("/"))
                .map(this::workingSheetLineParser)
                .reduce(new HashMap<>(), (a, b) -> {
                    a.putAll(b);
                    return a;
                });
    }
}
