package chat.occ.data;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ViewControllerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurerAdapter;

/**
 * Register view with controller using ViewControllerRegistry
 * Enable COR for login and logout
 */
@Configuration
public class ChatMvcWebConfig extends WebMvcConfigurerAdapter {

	
	/**
	 * ViewController will handle matching path, eg, '/viewroom'
	 * and render the view.
	 * This means that ChatController's RequestMapping(value="/viewroom")
	 * method would not be executed.
	 */
	@Override
	public void addViewControllers(ViewControllerRegistry registry) {
		registry.addViewController("/login").setViewName("login");
		registry.addViewController("/").setViewName("viewroom");
		registry.addViewController("/view/room").setViewName("viewroom");
		registry.addViewController("/view/msg").setViewName("viewmsg");

	}
}
