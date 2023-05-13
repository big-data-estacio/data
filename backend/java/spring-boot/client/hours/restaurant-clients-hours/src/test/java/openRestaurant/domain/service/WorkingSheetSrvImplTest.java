package openRestaurant.domain.service;

import org.apache.commons.lang3.tuple.Pair;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit.jupiter.SpringExtension;

import java.time.DayOfWeek;
import java.time.LocalTime;
import java.util.AbstractMap;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

import static org.junit.jupiter.api.Assertions.assertTrue;

@SpringBootTest(classes = {WorkingSheetSrvImpl.class, WorkingDaysSrvImpl.class, WorkingHoursSrvImpl.class})
@ExtendWith(SpringExtension.class)
class WorkingSheetSrvImplTest {

    @Autowired
    private WorkingSheetSrvImpl workingSheetSrvImpl;

    @Test
    void parseWorkingSheet() {
        String workingSheetStr = "Mon-Mon, Sun 11:30 am - 10 pm ";
        var expected = new HashMap<DayOfWeek, Map.Entry<LocalTime, LocalTime>>();
        expected.put(DayOfWeek.MONDAY, new AbstractMap.SimpleEntry<>(LocalTime.of(11, 30), LocalTime.of(22, 0).minusNanos(1L)));
        expected.put(DayOfWeek.SUNDAY, new AbstractMap.SimpleEntry<>(LocalTime.of(11, 30), LocalTime.of(22, 0).minusNanos(1L)));
        var actual = workingSheetSrvImpl.parseWorkingSheet(workingSheetStr);
        assertTrue(expected.keySet().stream().allMatch(actual::containsKey));
    }

    @Test
    void parseWorkingSheet_CrossNight() {
        String workingSheetStr = "Mon-Mon, Sun 11:30 am - 1 am ";
        var expected = new HashMap<DayOfWeek, Set<Pair<LocalTime, LocalTime>>>();
        expected.put(DayOfWeek.SUNDAY, Set.of(
                Pair.of(LocalTime.of(11, 30), LocalTime.of(23, 0).minusNanos(1L))));
        expected.put(DayOfWeek.MONDAY, Set.of(
                Pair.of(LocalTime.of(11, 30), LocalTime.of(23, 0).minusNanos(1L)),
                Pair.of(LocalTime.of(0, 0), LocalTime.of(1, 0).minusNanos(1L))));
        expected.put(DayOfWeek.TUESDAY, Set.of(
                Pair.of(LocalTime.of(0, 0), LocalTime.of(1, 0).minusNanos(1L))));
        var actual = workingSheetSrvImpl.parseWorkingSheet(workingSheetStr);
        assertTrue(expected.keySet().stream().allMatch(actual::containsKey));
    }

    @Test
    void parseWorkingSheet_Full() {
        String workingSheetStr = "Mon-Thu 11 am - 10:30 pm  / Fri 11 am - 11 pm  / Sat 11:30 am - 11 pm  / Sun 4:30 pm - 10:30 pm";
        var expected = new HashMap<DayOfWeek, Map.Entry<LocalTime, LocalTime>>();
        expected.put(DayOfWeek.MONDAY, new AbstractMap.SimpleEntry<>(LocalTime.of(11, 0), LocalTime.of(22, 30).minusNanos(1L)));
        expected.put(DayOfWeek.TUESDAY, new AbstractMap.SimpleEntry<>(LocalTime.of(11, 0), LocalTime.of(22, 30).minusNanos(1L)));
        expected.put(DayOfWeek.WEDNESDAY, new AbstractMap.SimpleEntry<>(LocalTime.of(11, 0), LocalTime.of(22, 30).minusNanos(1L)));
        expected.put(DayOfWeek.THURSDAY, new AbstractMap.SimpleEntry<>(LocalTime.of(11, 0), LocalTime.of(22, 30).minusNanos(1L)));
        expected.put(DayOfWeek.FRIDAY, new AbstractMap.SimpleEntry<>(LocalTime.of(11, 0), LocalTime.of(23, 0).minusNanos(1L)));
        expected.put(DayOfWeek.SATURDAY, new AbstractMap.SimpleEntry<>(LocalTime.of(11, 30), LocalTime.of(23, 0).minusNanos(1L)));
        expected.put(DayOfWeek.SUNDAY, new AbstractMap.SimpleEntry<>(LocalTime.of(16, 30), LocalTime.of(22, 30).minusNanos(1L)));
        var actual = workingSheetSrvImpl.parseWorkingSheet(workingSheetStr);
        assertTrue(expected.keySet().stream().allMatch(actual::containsKey));
    }
}