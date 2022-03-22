package com.trainticket.repository;

import com.trainticket.entity.Payment;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

/**
 * @author fdse
 */
public interface PaymentRepository extends MongoRepository<Payment,String> {

    Payment findById(String id);

    Payment findByOrderId(String orderId);

    @Override
    List<Payment> findAll();

    List<Payment> findByUserId(String userId);
}
