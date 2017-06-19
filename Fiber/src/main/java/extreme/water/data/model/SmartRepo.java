package extreme.water.data.model;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import extreme.water.data.model.Organization;

@Repository
public interface SmartRepo extends CrudRepository<Organization, Long> {

	public List<Organization> findAll();
	
}