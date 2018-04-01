package com.solx.repo;

import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.solx.domain.Usr;

public interface UsrRepo extends MongoRepository<Usr, String>{
	
    public Usr findByPhoneOffice(String officePhone);
    public Usr findByPhoneHome(String homePhone);
    public Usr findByEmail(String email);
    public List<Usr> findByCity(String city);
    public List<Usr> findByState(String state);
    
}
