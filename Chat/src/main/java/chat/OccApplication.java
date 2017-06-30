package chat;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Import;

import chat.occ.ChatApplication;
import chat.occ.ParseCmdLine;
import chat.occ.data.ChatMsgUserPersistence;
import chat.occ.data.ChatWsconfig;
import chat.occ.data.repo.RepositoryConfig;

@SpringBootApplication
@ComponentScan(basePackageClasses = { ChatMsgUserPersistence.class, ParseCmdLine.class, ChatApplication.class })
@Import({ RepositoryConfig.class, ChatWsconfig.class })
public class OccApplication {

	public static void main(String[] args) {
		SpringApplication.run(OccApplication.class, args);
	}
}
