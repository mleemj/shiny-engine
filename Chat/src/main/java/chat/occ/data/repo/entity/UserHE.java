package chat.occ.data.repo.entity;

import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;

import javax.persistence.Basic;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(schema = "chat_room_schema", name = "user")
public class UserHE {
    private Long usrId;
    private String usrName;
    private String usrEmail;
    private String usrPassword;
    private String usrRole;
    private String usrEnabled;

    @Id
    @Column(name = "usr_id")
    public Long getUsrId() {
        return usrId;
    }

    public void setUsrId(Long usrId) {
        this.usrId = usrId;
    }

    @Basic
    @Column(name = "usr_name", nullable = false, length = 16)
    public String getUsrName() {
        return usrName;
    }

    public void setUsrName(String usrName) {
        this.usrName = usrName;
    }

    @Basic
    @Column(name = "usr_email", nullable = false)
    public String getUsrEmail() {
        return usrEmail;
    }

    public void setUsrEmail(String usrEmail) {
        this.usrEmail = usrEmail;
    }

    @Basic
    @Column(name = "usr_password", nullable = false, length = 32)
    public String getUsrPassword() {
        return usrPassword;
    }

    public void setUsrPassword(String usrPassword) {
        this.usrPassword = usrPassword;
    }

    @Basic
    @Column(name = "usr_role", nullable = false, length = 45)
    public String getUsrRole() {
        return usrRole;
    }

    public void setUsrRole(String usrRole) {
        this.usrRole = usrRole;
    }

    @Basic
    @Column(name = "usr_enabled", nullable = false)
    public String getUsrEnabled() {
        return usrEnabled;
    }

    public void setUsrEnabled(String usrEnabled) {
        this.usrEnabled = usrEnabled;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;

        if (o == null || getClass() != o.getClass()) return false;

        UserHE userHE = (UserHE) o;

        return new EqualsBuilder()
                .append(usrId, userHE.usrId)
                .isEquals();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder(17, 37)
                .append(usrId)
                .toHashCode();
    }
}