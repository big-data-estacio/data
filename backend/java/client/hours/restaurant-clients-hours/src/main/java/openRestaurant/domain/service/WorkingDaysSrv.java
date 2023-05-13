package openRestaurant.domain.service;

import org.apache.commons.lang3.tuple.Pair;
import org.springframework.lang.NonNull;

import java.time.DayOfWeek;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;
import java.util.stream.IntStream;

public interface WorkingDaysSrv {

    default DayOfWeek parseDayString(@NonNull String dayOfWeek) {
        Objects.requireNonNull(dayOfWeek);
        switch (dayOfWeek.trim().toLowerCase()) {
            case "sat":
                return DayOfWeek.SATURDAY;
            case "sun":
                return DayOfWeek.SUNDAY;
            case "mon":
                return DayOfWeek.MONDAY;
            case "tue":
                return DayOfWeek.TUESDAY;
            case "wed":
                return DayOfWeek.WEDNESDAY;
            case "thu":
                return DayOfWeek.THURSDAY;
            case "fri":
                return DayOfWeek.FRIDAY;
            default:
                throw new IllegalArgumentException(String.format("invalid input: %s", dayOfWeek));
        }
    }

    default Set<DayOfWeek> calcWorkingDays(@NonNull DayOfWeek dayFrom, @NonNull DayOfWeek dayTo) throws IllegalArgumentException {
        //ex Mon-Fri
        int fromDay = dayFrom.getValue();
        int toDay = dayTo.getValue();
        if (fromDay > toDay)
            throw new IllegalArgumentException("From day must be less than or equal to day");
        Set<DayOfWeek> initialSet = new HashSet<>();
        IntStream.rangeClosed(fromDay, toDay)
                .forEach(i ->
                        initialSet.add(DayOfWeek.of(i))
                );
        return initialSet;
    }

    default Pair<DayOfWeek, DayOfWeek> extractPairs(@NonNull String daysPair) {
        Objects.requireNonNull(daysPair);
        var daysSplit = daysPair.split("-");
        if (daysSplit.length != 2)
            throw new IllegalArgumentException("expected string contains '-' ");
        return Pair.of(parseDayString(daysSplit[0]), parseDayString(daysSplit[1]));
    }

    default Set<DayOfWeek> parseWorkingDaysSheet(@NonNull String workingSheetStr) {
        Objects.requireNonNull(workingSheetStr);
        // ex "Mon-Thu, Sun";
        return Arrays.stream(workingSheetStr.split(","))
                .map(i -> {
                    if (!i.contains("-"))
                        i = String.format("%s-%s", i, i);
                    return extractPairs(i);
                }).map(p -> calcWorkingDays(p.getKey(), p.getValue()))
                .reduce(new HashSet<>(), (a, b) -> {
                    a.addAll(b);
                    return a;
                });
    }

}
