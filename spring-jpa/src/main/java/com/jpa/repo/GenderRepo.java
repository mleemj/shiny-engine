package com.jpa.repo;

import org.springframework.data.repository.CrudRepository;

import com.jpa.model.Gender;

public interface GenderRepo extends CrudRepository<Gender, Integer> {

}
