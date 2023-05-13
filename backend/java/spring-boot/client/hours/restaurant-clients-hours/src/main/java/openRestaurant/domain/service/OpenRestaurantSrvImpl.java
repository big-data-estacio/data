package openRestaurant.domain.service;

import openRestaurant.domain.model.Restaurant;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.lang.NonNull;
import org.springframework.lang.Nullable;
import org.springframework.stereotype.Service;
import utils.CSVContent;

import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;
import java.util.stream.Collectors;

@Service
public class OpenRestaurantSrvImpl implements OpenRestaurantSrv {
    private static final Logger LOGGER = LoggerFactory.getLogger(OpenRestaurantSrvImpl.class);

    private final WorkingSheetSrvImpl workingSheetSrvImpl;

    public OpenRestaurantSrvImpl(@Autowired WorkingSheetSrvImpl workingSheetSrvImpl) {
        this.workingSheetSrvImpl = workingSheetSrvImpl;
    }

    public Restaurant builder(@Nullable UUID id, @NonNull String[] dataRow) {
        //ex:Kyoto Sushi,Mon-Thu 11 am - 10:30 pm  / Fri 11 am - 11 pm  / Sat 11:30 am - 11 pm  / Sun 4:30 pm - 10:30 pm,,,
        LOGGER.info("building restaurant object from raw data : {}", String.join(",", dataRow));
        Objects.requireNonNull(dataRow);
        if (dataRow.length < 2)
            LOGGER.error("invalid data format: {}", String.join(",", dataRow));
        var restaurantName = dataRow[0].trim();
        if (restaurantName.length() == 0)
            LOGGER.error("invalid restaurant name format: {}", restaurantName);
        var workingSheetStr = dataRow[1].trim();
        if (workingSheetStr.length() == 0)
            LOGGER.error("invalid working sheet format: {}", workingSheetStr);
        var workingSheetMap = workingSheetSrvImpl.parseWorkingSheet(workingSheetStr);
        return new Restaurant(Optional.ofNullable(id).orElse(UUID.randomUUID()), restaurantName, workingSheetMap);
    }

    public List loadFromCSV(@NonNull String filePath) throws IOException {
        LOGGER.info("loading data from file: {}", filePath);
        Objects.requireNonNull(filePath);
        return CSVContent.getInstance(filePath)
                .getFileContent()
                .stream()
                .map(dataRow -> this.builder(null, dataRow))
                .collect(Collectors.toList());
    }

    public List<Restaurant> findOpenRestaurant(@NonNull String filePath, @NonNull String dateTime) throws IOException {
        Objects.requireNonNull(filePath);
        Objects.requireNonNull(dateTime);
        LOGGER.info("find open restaurant at file: {}, at dateTime {}", filePath, dateTime);
        var data = this.loadFromCSV(filePath);
        return findOpenRestaurants(data, LocalDateTime.parse(dateTime, DateTimeFormatter.ofPattern("yyyy-MM-dd h:m a")));
    }

    public List findOpenRestaurant(@NonNull String filePath, @NonNull LocalDateTime dateTime) throws IOException {
        Objects.requireNonNull(filePath);
        Objects.requireNonNull(dateTime);
        LOGGER.info("find open restaurant at file: {}, at dateTime {}", filePath, dateTime.toString());
        var data = this.loadFromCSV(filePath);
        return findOpenRestaurants(data, dateTime);
    }

    public List findOpenRestaurantsFromRawData(@NonNull List<String[]> rawData, @NonNull LocalDateTime dateTime) {
        Objects.requireNonNull(rawData);
        Objects.requireNonNull(dateTime);
        LOGGER.info("find open restaurant from raw data, at dateTime {}", dateTime.toString());
        var restaurants = rawData.stream().map(d -> this.builder(null, d))
                .collect(Collectors.toList());
        return findOpenRestaurants(restaurants, dateTime);
    }
}
