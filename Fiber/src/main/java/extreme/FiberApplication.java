package extreme;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Import;

import extreme.water.data.SmartApp;
import extreme.water.data.SmartConfig;

@SpringBootApplication
@ComponentScan(basePackageClasses={SmartApp.class})
@Import({SmartConfig.class})
public class FiberApplication {

	public static void main(String[] args) {
		SpringApplication.run(FiberApplication.class, args);
	}
}
