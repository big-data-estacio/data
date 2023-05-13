package openRestaurant.API;

import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.Resource;
import org.springframework.http.HttpStatus;
import org.springframework.lang.Nullable;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.server.ResponseStatusException;

import openRestaurant.domain.model.Restaurant;
import openRestaurant.domain.service.OpenRestaurantSrv;
import utils.CSVContent;

@RestController
public class RestaurantController {

    private final OpenRestaurantSrv openRestaurantSrv;

    @Value("classpath:rest_hours.csv")
    private Resource csvFile;

    private RestaurantController restaurantService;

    public RestaurantController(@Autowired OpenRestaurantSrv openRestaurantSrv) {
        this.openRestaurantSrv = openRestaurantSrv;
    }

    @RequestMapping("/restaurants/{now}")
    @ResponseStatus(HttpStatus.OK)
    public @ResponseBody
    List<Restaurant> findOpenRestaurants(@Nullable @PathVariable String now) throws IOException {
        var content = CSVContent.getInstance(csvFile.getURI().getPath()).getFileContent();
        var param = Optional.ofNullable(now)
                .map(n -> {
                    try {
                        return LocalDateTime.parse(n, DateTimeFormatter.ofPattern("yyyy-MM-dd h:m a"));
                    } catch (DateTimeParseException ex) {
                        throw new ResponseStatusException(HttpStatus.BAD_REQUEST, ex.getMessage(), ex);
                    }
                })
                .orElse(LocalDateTime.now());
        return openRestaurantSrv.findOpenRestaurantsFromRawData(content, param);
    }

    @RequestMapping("/restaurants/details/{id}")
    @ResponseStatus(HttpStatus.OK)
    public @ResponseBody Restaurant getRestaurantDetails(@Nullable @PathVariable String id) throws IOException {
        // Substitua este código pela lógica real para obter os detalhes do restaurante
        // Aqui, assumimos que você tem um serviço chamado restaurantService que tem um método getRestaurantDetails

        if (id == null) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "ID do restaurante não fornecido");
        }

        Restaurant restaurant = restaurantService.getRestaurantDetails(id);
        if (restaurant == null) {
            throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Restaurante não encontrado");
        }

        return restaurant;
    }

    // @RequestMapping("/restaurants/{id}")
    // @ResponseStatus(HttpStatus.OK)
    // public @ResponseBody Restaurant getRestaurantById(@PathVariable("id") Integer id) throws IOException {
    //     var content = CSVContent.getInstance(csvFile.getURI().getPath()).getFileContent();

    //     // Procurando o restaurante pelo ID
    //     Optional<Restaurant> restaurantOpt = content.stream()
    //                                                 .filter(r -> r.getId().equals(id))
    //                                                 .findFirst();

    //     if (!restaurantOpt.isPresent()) {
    //         throw new ResponseStatusException(HttpStatus.NOT_FOUND, "Restaurante não encontrado");
    //     }

    //     return restaurantOpt.get();
    // }

    // @PostMapping("/restaurants")
    // @ResponseStatus(HttpStatus.CREATED)
    // public @ResponseBody Restaurant createRestaurant(@Valid @RequestBody Restaurant newRestaurant) throws IOException {
    //     // Verifica se os campos obrigatórios estão presentes
    //     if (newRestaurant.getId() == null || newRestaurant.getCliente() == null || newRestaurant.getHorario() == null) {
    //         throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Os campos id, cliente e horario são obrigatórios");
    //     }

    //     // Verifica se o ID do restaurante já existe
    //     if (restaurantService.doesRestaurantExist(newRestaurant.getId())) {
    //         throw new ResponseStatusException(HttpStatus.CONFLICT, "Um restaurante com este ID já existe");
    //     }

    //     Restaurant restaurant = restaurantService.addRestaurant(newRestaurant);

    //     if (restaurant == null) {
    //         throw new ResponseStatusException(HttpStatus.INTERNAL_SERVER_ERROR, "Falha ao criar o restaurante");
    //     }

    //     return restaurant;
    // }

}
