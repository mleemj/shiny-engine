package chat.occ;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ChatController {
	private Logger logger = LoggerFactory.getLogger(ChatController.class);

	@RequestMapping("/api/msg")
	public String chatlogin(@RequestParam(value="username") String username,
			@RequestParam(value="password")String password){
		logger.info("------ inside ChatController ------");
		return "Hello ".concat(username).concat(" ").concat(password);
	}
}
