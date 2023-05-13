package openRestaurant.domain.service;

import org.apache.commons.lang3.tuple.Pair;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit.jupiter.SpringExtension;

import java.time.DayOfWeek;
import java.time.LocalTime;
import java.util.HashMap;
import java.util.Set;

@SpringBootTest(classes = {WorkingDaysSrvImpl.class, WorkingHoursSrvImpl.class})
@ExtendWith(SpringExtension.class)
public class WorkingHoursTest {

    @Autowired
    private WorkingHoursSrv workingHoursSrv;

    @Test
    void calcWorkingHours() {
        var duration = new HashMap<DayOfWeek, Set<Pair<LocalTime, LocalTime>>>();
        duration.put(DayOfWeek.MONDAY, Set.of(Pair.of(LocalTime.of(11, 30), LocalTime.of(21, 00).minusNanos(1L))));
        Assertions.assertEquals(duration, workingHoursSrv.calcWorkingHours(DayOfWeek.MONDAY, "11:30 am - 9 pm"));
    }
}
