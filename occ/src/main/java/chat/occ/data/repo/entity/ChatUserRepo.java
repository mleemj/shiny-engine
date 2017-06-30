package chat.occ.data.repo.entity;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ChatUserRepo extends CrudRepository<UserHE, Long> {
	
	public List<UserHE> findAll();
	
	public UserHE findByUsrEmail(String usrEmail);
}
