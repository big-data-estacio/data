import openRestaurant.domain.service.*;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.core.io.Resource;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import utils.CSVContent;

@SpringBootTest(classes = {OpenRestaurantSrvImpl.class, WorkingSheetSrvImpl.class, WorkingDaysSrvImpl.class, WorkingHoursSrvImpl.class, CSVContent.class})
@ExtendWith(SpringExtension.class)
class ApplicationTest {

    @Value("classpath:rest_hours.csv")
    private Resource csvFile;

    @Autowired
    private OpenRestaurantSrvImpl openRestaurantSrvImpl;

    @Test
    void run() throws Exception {
        Application application = new Application(openRestaurantSrvImpl);
        var filePath = csvFile.getURI().getPath();
        var dateTime = "2019-05-15 1:00 AM";
        application.run(filePath, dateTime);
    }
}