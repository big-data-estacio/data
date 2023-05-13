package openRestaurant.domain.service;

import org.apache.commons.lang3.tuple.Pair;
import org.springframework.lang.NonNull;

import java.time.DayOfWeek;
import java.time.LocalTime;
import java.util.Map;
import java.util.Set;

public interface WorkingSheetSrv {

    String DAYS_PATTERN = "(^\\D{3}\\s*,\\s*\\D{3}-\\s*\\D{3})|(^\\D{3}-\\D{3}\\s*(,\\s*\\D{3})?)|(^\\D{3}(-\\s*\\D{3})?\\s*(,\\s*\\D{3})?)";

    Map<DayOfWeek, Set<Pair<LocalTime, LocalTime>>> workingSheetLineParser(@NonNull String workingSheetStr);

    Map<DayOfWeek, Set<Pair<LocalTime, LocalTime>>> parseWorkingSheet(@NonNull String workingSheetStr);
}
