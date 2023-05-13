package openRestaurant.domain.service;

import openRestaurant.domain.model.Restaurant;
import org.apache.commons.lang3.tuple.Pair;
import org.junit.jupiter.api.*;
import org.junit.jupiter.api.extension.ExtendWith;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.core.io.Resource;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import utils.CSVContent;

import java.io.IOException;
import java.time.DayOfWeek;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.*;
import java.util.stream.Collectors;

import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

@SpringBootTest(classes = {OpenRestaurantSrvImpl.class, WorkingSheetSrvImpl.class, WorkingDaysSrvImpl.class, WorkingHoursSrvImpl.class})
@ExtendWith(SpringExtension.class)
class OpenRestaurantSrvImplTest {
    private static final Logger LOGGER = LoggerFactory.getLogger(OpenRestaurantSrvImplTest.class);

    private final Resource csvFile;
    private final CSVContent csvContent;

    @Autowired
    private OpenRestaurantSrvImpl openRestaurantSrvImpl;

    public OpenRestaurantSrvImplTest(@Value("classpath:rest_hours.csv") Resource csvFile) throws IOException {
        this.csvFile = csvFile;
        this.csvContent = CSVContent.getInstance(csvFile.getURI().getPath());
    }

    @BeforeAll
    static void setup() {
        LOGGER.info("starting unit test");
    }

    @BeforeEach
    void beforeEach() {
        assertTrue(csvFile.exists());
    }

    @Test
    void loadCSVFile() {
        assertNotNull(csvContent.getFileContent());
        LOGGER.info("printing file content");
    }

    @Test
    void loadOneRestaurant() {
        List<String[]> csvData = new ArrayList<>() {{
            add("Kyoto Sushi,Mon-Thu 11 am - 10:30 pm  / Fri 11 am - 11 pm  / Sat 11:30 am - 11 pm  / Sun 4:30 pm - 10:30 pm,,,"
                    .split(","));
        }};

        var id = UUID.randomUUID();
        var restaurantName = "Kyoto Sushi";
        var workingSheetMap = new HashMap<DayOfWeek, Set<Pair<LocalTime, LocalTime>>>();
        workingSheetMap.put(DayOfWeek.MONDAY, Set.of(Pair.of(LocalTime.of(11, 0), LocalTime.of(22, 30))));
        workingSheetMap.put(DayOfWeek.TUESDAY, Set.of(Pair.of(LocalTime.of(11, 0), LocalTime.of(22, 30))));
        workingSheetMap.put(DayOfWeek.WEDNESDAY, Set.of(Pair.of(LocalTime.of(11, 0), LocalTime.of(22, 30))));
        workingSheetMap.put(DayOfWeek.THURSDAY, Set.of(Pair.of(LocalTime.of(11, 0), LocalTime.of(22, 30))));
        workingSheetMap.put(DayOfWeek.FRIDAY, Set.of(Pair.of(LocalTime.of(11, 0), LocalTime.of(23, 0))));
        workingSheetMap.put(DayOfWeek.SATURDAY, Set.of(Pair.of(LocalTime.of(11, 30), LocalTime.of(23, 0))));
        workingSheetMap.put(DayOfWeek.SUNDAY, Set.of(Pair.of(LocalTime.of(16, 30), LocalTime.of(22, 30))));

        var expected = new Restaurant(id, restaurantName, workingSheetMap);

        List<Restaurant> data = csvData.stream().parallel()
                .map(dataRow -> openRestaurantSrvImpl.builder(id, dataRow))
                .collect(Collectors.toList());
        Assertions.assertNotNull(data);
        Assertions.assertFalse(data.stream().findAny().isEmpty());
        Assertions.assertEquals(expected.getId(), data.stream().findAny().get().getId());
        Assertions.assertEquals(expected.getName(), data.stream().findAny().get().getName());

        var actual = openRestaurantSrvImpl.findOpenRestaurants(data, LocalDateTime.parse("2019-05-15 7:00 AM",
                DateTimeFormatter.ofPattern("yyyy-MM-dd h:m a")));
        Assertions.assertEquals(0, actual.size());
    }

    @Test
    void loadOneRestaurantOverNight() {
        List<String[]> csvData = new ArrayList<>() {{
            add("Sudachi,Mon-Wed 5 pm - 12:30 am  / Thu-Fri 5 pm - 1:30 am  / Sat 3 pm - 1:30 am  / Sun 3 pm - 11:30 pm,,,"
                    .split(","));
            add("Penang Garden,Mon-Thu 11 am - 10 pm  / Fri-Sat 10 am - 10:30 pm  / Sun 11 am - 11 pm,,,"
                    .split(","));
        }};
        var id = UUID.randomUUID();
        var restaurantName = "Sudachi";
        var workingSheetMap = new HashMap<DayOfWeek, Set<Pair<LocalTime, LocalTime>>>();
        workingSheetMap.put(DayOfWeek.MONDAY, Set.of(Pair.of(LocalTime.of(17, 0), LocalTime.of(0, 30))));
        workingSheetMap.put(DayOfWeek.TUESDAY, Set.of(Pair.of(LocalTime.of(17, 0), LocalTime.of(0, 30))));
        workingSheetMap.put(DayOfWeek.WEDNESDAY, Set.of(Pair.of(LocalTime.of(17, 0), LocalTime.of(0, 30))));
        workingSheetMap.put(DayOfWeek.THURSDAY, Set.of(Pair.of(LocalTime.of(17, 0), LocalTime.of(1, 30))));
        workingSheetMap.put(DayOfWeek.SATURDAY, Set.of(Pair.of(LocalTime.of(15, 0), LocalTime.of(1, 30))));
        workingSheetMap.put(DayOfWeek.SUNDAY, Set.of(Pair.of(LocalTime.of(15, 0), LocalTime.of(23, 30))));

        var expected = new Restaurant(id, restaurantName, workingSheetMap);

        List<Restaurant> data = csvData
                .stream()
                .parallel()
                .map(dataRow -> openRestaurantSrvImpl.builder(id, dataRow))
                .collect(Collectors.toList());

        Assertions.assertNotNull(data);
        Assertions.assertFalse(data.stream().findAny().isEmpty());
        Assertions.assertEquals(expected.getId(), data.stream().findAny().get().getId());
        Assertions.assertEquals(expected.getName(), data.stream().findAny().get().getName());

        var actual = openRestaurantSrvImpl.findOpenRestaurants(data, LocalDateTime.parse("2019-05-15 7:00 PM",
                DateTimeFormatter.ofPattern("yyyy-MM-dd h:m a")));
        Assertions.assertEquals(2, actual.size());
    }

    @Test
    void loadRestaurantFromCSV() throws IOException {
        var recordCount = 51;
        var filePath = csvFile.getURI().getPath();
        List restaurants = openRestaurantSrvImpl.loadFromCSV(filePath);
        Assertions.assertEquals(recordCount, restaurants.size());
    }

    @Test
    void findOpenRestaurant() throws IOException {
        var filePath = csvFile.getURI().getPath();
        var dateTime = LocalDateTime.parse("2019-05-12 11:59 PM", DateTimeFormatter.ofPattern("yyyy-MM-dd h:m a"));
        List restaurants = openRestaurantSrvImpl.findOpenRestaurant(filePath, dateTime);
        Assertions.assertTrue(restaurants.size() > 0);
    }

    @ParameterizedTest
    @ValueSource(strings = {"Hanuri,Mon-Sun 11 am - 12 am,,,"})
    void findOpenRestaurantTestDataSheet(String dataRow) throws IOException {
        var data = new ArrayList<String[]>() {{
            add(dataRow.split(","));
        }};

        List restaurants = openRestaurantSrvImpl.findOpenRestaurantsFromRawData(data,
                LocalDateTime.parse("2019-05-12 11:50 PM", DateTimeFormatter.ofPattern("yyyy-MM-dd h:m a")));
        Assertions.assertTrue(restaurants.size() > 0);
    }

    @ParameterizedTest
    @ValueSource(strings = {"2019-05-12 11:50 PM", "2019-05-13 11:0 AM"})
    void findOpenRestaurantTestDateTime(String dateTime) throws IOException {
        var data = new ArrayList<String[]>() {{
            add("Hanuri,Mon-Sun 11 am - 1 am,,,".split(","));
        }};

        List restaurants = openRestaurantSrvImpl.findOpenRestaurantsFromRawData(data,
                LocalDateTime.parse(dateTime, DateTimeFormatter.ofPattern("yyyy-MM-dd h:m a")));
        Assertions.assertTrue(restaurants.size() > 0);
    }

    @ParameterizedTest
    @ValueSource(strings = {"2019-05-12 11:0 PM", "2019-05-13 10:0 AM"})
    void findOpenRestaurantTestOutOfDateTime(String dateTime) throws IOException {
        var data = new ArrayList<String[]>() {{
            add("Hanuri,Mon-Sun 11 am - 11 pm,,,".split(","));
        }};

        List restaurants = openRestaurantSrvImpl.findOpenRestaurantsFromRawData(data,
                LocalDateTime.parse(dateTime, DateTimeFormatter.ofPattern("yyyy-MM-dd h:m a")));
        Assertions.assertEquals(0, restaurants.size());
    }

    @AfterAll
    static void cleanUp() {
        LOGGER.info("finishing unit test.");
    }
}