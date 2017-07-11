package chat.occ.data.model;

import java.security.Key;
import java.util.HashMap;
import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import io.jsonwebtoken.JwtException;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.impl.crypto.MacProvider;

public class ChatJwtHelper{
	static String EMAIL = "usrEmail";
	static Logger logger = LoggerFactory.getLogger(ChatJwtHelper.class);

	public static String getToken(ChatUser cu) {
		Map<String, Object> claims = new HashMap<>();
		claims.put(EMAIL, cu.getUsrEmail());
		String jwtString = Jwts.builder().setSubject(cu.getUsrName()).setClaims(claims)
				.signWith(SignatureAlgorithm.HS512, cu.getChatUsrJwtKey()).compact();
		return jwtString;
	}

	public static boolean checkToken(String jwt, ChatUser cu) {
		boolean isValid = true;
		try {
			Jwts.parser()
					.requireSubject(cu.getUsername())
					.require(EMAIL, cu.getUsrEmail())
					.setSigningKey(cu.getChatUsrJwtKey())
					.parseClaimsJws(jwt);
		} catch (JwtException e) {
			logger.info(e.getMessage());
			isValid = false;
		}
		return isValid;
	}

	public static Key generateKey() {
		Key secretKey = MacProvider.generateKey();
		return secretKey;
	}
}
