package chat.occ;

import java.io.InputStream;
import java.util.Scanner;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;

public class CsvFileParser implements CommandLineRunner {
	private ResourceLoader resourceLoader;

	@Autowired
	public CsvFileParser(ResourceLoader loader) {
		this.resourceLoader = loader;
	}

	@Override
	public void run(String... arg0) throws Exception {
		Logger logger = LoggerFactory.getLogger("ParseCmdLine");
		logger.info("----- inside ParseCmdLine -----");
		InputStream file = null;
		Scanner scanner = null;
		Resource resource = this.resourceLoader.getResource("classpath:sample_data.csv");
		file = resource.getInputStream();
		scanner = new Scanner(file);
		while (scanner.hasNextLine()) {
			logger.info(scanner.nextLine());
		}

		scanner.close();
		file.close();
		logger.info("----- end ParseCmdLine -----");
	}

}
