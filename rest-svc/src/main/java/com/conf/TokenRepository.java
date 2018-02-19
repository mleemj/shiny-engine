package com.conf;

import org.springframework.security.web.util.matcher.AntPathRequestMatcher;
import org.springframework.security.web.util.matcher.RequestMatcher;
import org.springframework.stereotype.Component;

/**
 * Demonstrates dependency injection through @Component and @Qualifier
 */
@Component("token-repository")
public class TokenRepository extends AbstractTokenRepository {

    @Override
    public String getCookieName() {
        return "smartcookie";
    }

    @Override
    public String getHeaderName() {
        return "smartheader";
    }

    @Override
    public RequestMatcher getRequireCsrfRequestMatcher() {
        return new AntPathRequestMatcher("/csrf");
    }
}