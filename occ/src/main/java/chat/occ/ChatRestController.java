package chat.occ;

import java.util.Optional;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ChatRestController {

	@CrossOrigin({"http://localhost" })
	@RequestMapping({ "/chat/success" })
	public Greeting sucessfulLogin() {
		Logger logger = LoggerFactory.getLogger("ChatRestController");
		logger.info("sucess login");

		return new Greeting(Optional.empty(), "Sucess logged in");
	}
}

class Greeting {

	private final long id;
	private final String content;

	public Greeting() {
		this.id = -1;
		this.content = "";
	}

	/**
	 * Uses Optional and Long primitive
	 */
	public Greeting(Optional<Long> option_id, String content) {
		this.id = option_id.orElse(-1L);
		this.content = content;
	}

	public long getId() {
		return id;
	}

	public String getContent() {
		return content;
	}
}