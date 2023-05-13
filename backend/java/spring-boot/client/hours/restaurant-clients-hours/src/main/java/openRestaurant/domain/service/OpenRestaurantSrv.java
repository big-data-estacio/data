package openRestaurant.domain.service;

import openRestaurant.domain.model.Restaurant;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.lang.NonNull;
import org.springframework.lang.Nullable;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Objects;
import java.util.UUID;
import java.util.stream.Collectors;

public interface OpenRestaurantSrv {
    Logger LOGGER = LoggerFactory.getLogger(OpenRestaurantSrv.class);

    Restaurant builder(@Nullable UUID id, @NonNull String[] dataRow);

    default List<Restaurant> findOpenRestaurants(@NonNull List<Restaurant> restaurants, @NonNull LocalDateTime dateTime) {
        Objects.requireNonNull(restaurants);
        Objects.requireNonNull(dateTime);
        var dayOfWeek = dateTime.getDayOfWeek();
        var time = dateTime.toLocalTime();
        return restaurants.stream().filter(r ->
                r.getWorkingHours().containsKey(dayOfWeek) &&
                        r.getWorkingHours().values().stream()
                                .anyMatch(t -> t.stream().
                                        anyMatch(tt -> tt.getLeft().compareTo(time) <= 0 && tt.getRight().compareTo(time) > 0)))
                .collect(Collectors.toList());
    }

    default List<Restaurant> findOpenRestaurantsFromRawData(@NonNull List<String[]> rawData, @NonNull LocalDateTime dateTime) {
        Objects.requireNonNull(rawData);
        Objects.requireNonNull(dateTime);
        LOGGER.info("find open restaurant from raw data, at dateTime {}", dateTime.toString());
        var restaurants = rawData.stream().map(d -> this.builder(null, d))
                .collect(Collectors.toList());
        return this.findOpenRestaurants(restaurants, dateTime);
    }
}
