package com.solx;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.Assert.assertEquals;

import java.util.List;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import com.solx.domain.Usr;
import com.solx.repo.UsrRepo;

@RunWith(SpringRunner.class)
@SpringBootTest
public class UserRepositoryTests {

	@Autowired
	UsrRepo repository;

	Usr dave, oliver, carter, ken;
	String chi = "Chicago";
	String npr = "Naperville";
	String illinois = "IL";
	String daveOffice = "D-123-456-7890";
	String daveHome = "D-123-456-7890";

	String oliverOffice = "A-123-456-7890";
	String oliverHome = "B-123-456-7890";

	String carterOffice = "C-123-456-7890";
	String carterHome = "C-123-456-7890";
	String carterEmail = "carter@email.com";

	String kenOffice = "K-123-456-7890";
	String kenHome = "K-123-456-7890";
	String kenEmail = "ken@email.com";

	@Before
	public void setUp() {
		repository.deleteAll();
	}

	@Test
	public void setsIdOnSave() {
		dave = Usr.makeUsr("Dave", "dave@email.com", daveOffice, daveHome);
		dave.setCity(chi);
		dave.setState(illinois);
		Usr d = repository.save(dave);

		assertThat(d.id).isNotNull();
	}

	@Test
	public void findsByPhone() {
		oliver = Usr.makeUsr("Oliver", "oliver@email.com", oliverOffice, oliverHome);
		oliver.setCity(npr);
		oliver.setState(illinois);
		repository.save(oliver);
		
		Usr oliverA = repository.findByPhoneHome(oliverHome);
		Usr oliverB = repository.findByPhoneOffice(oliverOffice);
		assertEquals(oliverA, oliverB);
	}

	@Test
	public void findsByLocation() {
		carter = Usr.makeUsr("Carter", carterEmail, carterOffice, carterHome);
		carter.setCity(chi);
		carter.setState(illinois);

		ken = Usr.makeUsr("Ken", kenEmail, kenOffice, kenHome);
		ken.setCity(npr);
		ken.setState(illinois);
		repository.save(carter);
		repository.save(ken);
		
		List<Usr> stateUsr = repository.findByState(illinois);
		assertEquals(2, stateUsr.size());

		List<Usr> citiUsr = repository.findByCity(chi);
		assertEquals(1, citiUsr.size());
	}
}