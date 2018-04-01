package com.solx;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import com.solx.domain.Usr;
import com.solx.repo.UsrRepo;

@SpringBootApplication
public class Application implements CommandLineRunner {

	@Autowired
	private CustomerRepository repository;
	
	@Autowired
	private UsrRepo userRepository;

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}

	@Override
	public void run(String... args) throws Exception {		
		userRepository.deleteAll();
		String chi = "Chicago";
		String npr = "Naperville";
		String Illinois = "IL";
		String aliceOffice = "1-123-456-7890";
		String aliceHome = "1-123-456-7890";
		Usr alice = Usr.makeUsr("Alice", "alice@email.com", aliceOffice, aliceHome);
		alice.setCity(chi);
		alice.setState(Illinois);
		
		String fredOffice = "2-123-456-7890";
		String fredHome = "2-123-456-7890";
		Usr fred = Usr.makeUsr("Fred", "fred@email.com", fredOffice, fredHome);
		fred.setCity(npr);
		fred.setState(Illinois);
		
		String johnOffice = "3-123-456-7890";
		String johnHome = "3-123-456-7890";
		String johnEmail = "john@email.com";
		Usr john = Usr.makeUsr("John", johnEmail, johnOffice, johnHome);
		john.setCity(chi);
		john.setState(Illinois);
		
		userRepository.save(alice);
		userRepository.save(fred);
		userRepository.save(john);
		
		//fetch all users
		System.out.println("Users found with findAll()");
		System.out.println("-------------------------------");
		for(Usr user: userRepository.findAll()) {
			System.out.println(user);
		}
		System.out.println();
		
		//fetch by office phone
		System.out.println("Users found with findByPhoneOffice");
		System.out.println("-------------------------------");
		Usr officeAlice = userRepository.findByPhoneOffice(aliceOffice);
		System.out.println(officeAlice);
		System.out.println();

		//fetch by home phone
		System.out.println("Users found with findByHomeOffice");
		System.out.println("-------------------------------");
		Usr homeFred = userRepository.findByPhoneHome(fredHome);
		System.out.println(homeFred);
		System.out.println();
		
		//fetch by email
		System.out.println("Users found with findByEmail");
		System.out.println("-------------------------------");
		Usr emailJohn = userRepository.findByEmail(johnEmail);
		System.out.println(emailJohn);
		System.out.println();
		
		//fetch by citi
		System.out.println("Users found with findByCity");
		System.out.println("-------------------------------");
		userRepository.findByCity(chi).stream().forEach(u -> System.out.println(u));
		System.out.println();
		
		//fetch by state
		System.out.println("Users found with findByState");
		System.out.println("-------------------------------");
		userRepository.findByState(Illinois).stream().forEach(u -> System.out.println(u));
		System.out.println();
	}

}
