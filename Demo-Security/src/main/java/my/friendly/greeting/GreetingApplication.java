package my.friendly.greeting;

import my.friendly.greeting.adapter.InterceptorConfig;
import my.friendly.greeting.adapter.SecurityConfig;
import my.friendly.greeting.adapter.TokenRepository;
import my.friendly.greeting.web.GreetingController;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Import;

/**
 * @SpringBootApplication consists of @Configuration,
 * @EnableAutoConfiguration, @ComponentScan
 *
 * @RestController is made up of @Controller and @ResponseBody
 *
 * @Controller is a specialized form of component
 */
@SpringBootApplication
@ComponentScan(basePackageClasses = {GreetingController.class,
		TokenRepository.class})
@Import({SecurityConfig.class, InterceptorConfig.class})
public class GreetingApplication {

	public static void main(String[] args) {
		SpringApplication.run(GreetingApplication.class, args);
	}
}
