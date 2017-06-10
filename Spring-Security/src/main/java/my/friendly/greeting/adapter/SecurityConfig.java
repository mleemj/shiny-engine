package my.friendly.greeting.adapter;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication
        .builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders
        .HttpSecurity;
import org.springframework.security.config.annotation.web.builders
        .WebSecurity;
import org.springframework.security.config.annotation.web.configuration
        .EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration
        .WebSecurityConfigurerAdapter;

/**
 * Extends AbstractTokenRepository and inject the custom
 * token repository into custom web security configuration.
 * <p>
 * Spring injects (@Autowired) customized CsrfTokenRepository
 *
 * @EnableWebSecurity creates springSecurityFilterChain and provides
 * a built-in CsrfTokenArgumentResolver which resolves CsrfToken for
 * GreetingController's method
 * <p>
 * public CsrfToken csrf(CsrfToken token){return token}
 */
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    private AbstractTokenRepository customCookieCsrTokenRepository;

    /**
     * TokenRepository @Component("token-repository") inform Spring
     */
    @Autowired
    @Qualifier("token-repository")
    public void setTokenRepository(AbstractTokenRepository
                                           repository) {
        this.customCookieCsrTokenRepository = repository;
    }

    /**
     * WebSecurity is to secure resources at global level
     */
    @Override
    public void configure(WebSecurity webSecurity) {
        webSecurity.ignoring().antMatchers("/", "/home");
    }

    /**
     * @Autowired marks a constructor, field, setter method or config method
     * as to be autowired by Spring's dependency injection facilities.
     */
    @Autowired
    public void configureGlobal(AuthenticationManagerBuilder auth) throws
            Exception {
        auth.inMemoryAuthentication()
                .withUser("user")
                .password("password")
                .roles("USER");
    }

    /**
     * Customize CookieCSRF repository and specify csrf protection
     */
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.csrf()
                .requireCsrfProtectionMatcher(
                        customCookieCsrTokenRepository
                                .getRequireCsrfRequestMatcher())
                .csrfTokenRepository(
                        customCookieCsrTokenRepository
                                .getTokenRepository());
        ;
    }

}