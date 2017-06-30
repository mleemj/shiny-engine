package extreme.water.data;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

import extreme.water.data.model.Organization;
import extreme.water.data.model.SmartRepo;

@Order(value = 1)
@Component
public class SmartApp implements CommandLineRunner {
	private SmartRepo smartRepository;
	
	@Autowired
	public SmartApp(SmartRepo smartRepo){
		this.smartRepository = smartRepo;
	}

	@Override
	public void run(String... arg0) throws Exception {
		System.out.println("_____ inside SmartApp _____");
		List<Organization> organizations = this.smartRepository.findAll();
		for(Organization org: organizations){
			System.out.println(org.getOrganizationName());
		}
	}

}
