package openRestaurant.domain.service;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit.jupiter.SpringExtension;

import java.time.DayOfWeek;
import java.util.Set;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

@SpringBootTest(classes = {WorkingDaysSrvImpl.class, WorkingHoursSrvImpl.class})
@ExtendWith(SpringExtension.class)
class WorkingDaysSrvTest {

    @Autowired
    private WorkingDaysSrv workingDaysSrv;

    @Test
    void parseDayString() {
        assertEquals(DayOfWeek.SUNDAY, workingDaysSrv.parseDayString("sun"));
    }

    @Test
    void parseDatString_CAPS() {
        assertEquals((DayOfWeek.MONDAY), workingDaysSrv.parseDayString("MON"));
    }

    @Test
    void calcWorkingDays() {
        assertEquals(Set.of(DayOfWeek.MONDAY, DayOfWeek.TUESDAY, DayOfWeek.WEDNESDAY),
                workingDaysSrv.calcWorkingDays(DayOfWeek.MONDAY, DayOfWeek.WEDNESDAY));
    }

    @Test
    void calcWorkingDays_MON_TO_SUN() {
        assertEquals(
                Set.of(DayOfWeek.MONDAY, DayOfWeek.TUESDAY, DayOfWeek.WEDNESDAY,
                        DayOfWeek.THURSDAY, DayOfWeek.FRIDAY, DayOfWeek.SATURDAY, DayOfWeek.SUNDAY),
                workingDaysSrv.calcWorkingDays(DayOfWeek.MONDAY, DayOfWeek.SUNDAY));
    }

    @Test
    void calcWorkingDays_THU_TO_WED() {
        assertThrows(
                IllegalArgumentException.class,
                () -> workingDaysSrv.calcWorkingDays(DayOfWeek.THURSDAY, DayOfWeek.WEDNESDAY));
    }

    @ParameterizedTest
    @ValueSource(strings = {"Mon-Thu, Sun", "Sun, Mon-Thu"})
    void parseWorkingDays(String workingDaysStr) {
        var workingSheet = Set.of(DayOfWeek.MONDAY, DayOfWeek.THURSDAY, DayOfWeek.TUESDAY, DayOfWeek.WEDNESDAY, DayOfWeek.SUNDAY);
        assertEquals(workingSheet, workingDaysSrv.parseWorkingDaysSheet(workingDaysStr));
    }


}