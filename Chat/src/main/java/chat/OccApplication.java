package chat;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Import;

import chat.occ.ChatApplication;
import chat.occ.ChatController;
import chat.occ.data.ChatUsrPersistence;
import chat.occ.data.SecurityConfig;
import chat.occ.data.repo.RepositoryConfig;

@SpringBootApplication
@ComponentScan(basePackageClasses = { ChatUsrPersistence.class, ChatApplication.class, ChatController.class })
@Import({ RepositoryConfig.class, SecurityConfig.class})
public class OccApplication {

	public static void main(String[] args) {
		SpringApplication.run(OccApplication.class, args);
	}
}
