package travel.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.repository.CrudRepository;
import travel.entity.Trip;
import travel.entity.TripId;

import java.util.ArrayList;

/**
 * @author fdse
 */
public interface TripRepository extends MongoRepository<Trip,TripId> {

    Trip findByTripId(TripId tripId);

    void deleteByTripId(TripId tripId);

    @Override
    ArrayList<Trip> findAll();

    ArrayList<Trip> findByRouteId(String routeId);
}
