package openRestaurant.API;

import openRestaurant.domain.service.OpenRestaurantSrvImpl;
import openRestaurant.domain.service.WorkingDaysSrvImpl;
import openRestaurant.domain.service.WorkingHoursSrvImpl;
import openRestaurant.domain.service.WorkingSheetSrvImpl;
import org.junit.jupiter.api.*;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;

import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@ExtendWith(SpringExtension.class)
@WebMvcTest
@AutoConfigureMockMvc
@ContextConfiguration(classes = {RestaurantController.class, OpenRestaurantSrvImpl.class, WorkingSheetSrvImpl.class, WorkingDaysSrvImpl.class, WorkingHoursSrvImpl.class})
class RestaurantControllerTest {

    @Autowired
    private MockMvc mockMvc;


    @BeforeEach
    void setUp() {
        Assertions.assertNotNull(mockMvc);
    }

    @AfterEach
    void tearDown() {
    }

    @Test
    void successResponse() throws Exception {
        mockMvc.perform(MockMvcRequestBuilders.get("/restaurants/2019-05-15 11:00 AM")
                .contentType(MediaType.APPLICATION_JSON)
                .accept(MediaType.APPLICATION_JSON))
                .andDo(print())
                .andExpect(status().isOk());

    }
}