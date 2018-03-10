package com.jpa;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.boot.test.autoconfigure.orm.jpa.TestEntityManager;
import org.springframework.test.context.junit4.SpringRunner;

import com.jpa.model.Gender;
import com.jpa.repo.GenderRepo;

@RunWith(SpringRunner.class)
@DataJpaTest
public class GenderRepoTest {
	private Logger log = LoggerFactory.getLogger(GenderRepoTest.class);
			
	@Autowired
	private TestEntityManager entityManager;
	
	@Autowired
	private GenderRepo repo;

	@Test
	public void test() {
		Gender gender = new Gender(0);
		entityManager.persist(gender);
		
		for(Gender g :repo.findAll()) {
			log.info(g.getPassengerId() + " " + g.getSurvived());
		}
		log.info("++++++++++++++++++++++++++++++++++++++++++++++++");
	}

}