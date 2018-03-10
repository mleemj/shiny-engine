package com.jpa;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import com.jpa.model.Gender;
import com.jpa.repo.GenderRepo;

@SpringBootApplication
public class JpaApplication {
	private static final Logger log = LoggerFactory.getLogger(JpaApplication.class);

	public static void main(String[] args) {
		SpringApplication.run(JpaApplication.class);
	}

	@Bean
	public CommandLineRunner demo(GenderRepo repository) {
		return (args) -> {

			// fetch all customers
			log.info("GenderRepo found with findAll():");
			Gender g = new Gender(0);
			repository.save(g);
			for (Gender gender : repository.findAll()) {
				log.info(gender.getPassengerId().toString());
			}
			log.info("-------------------------------");
		};
	}
}