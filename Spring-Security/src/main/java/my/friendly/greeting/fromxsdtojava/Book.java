
package my.friendly.greeting.fromxsdtojava;

import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import javax.annotation.Generated;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>Java class for anonymous complex type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * 
 * <pre>
 * &lt;complexType>
 *   &lt;complexContent>
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       &lt;sequence>
 *         &lt;element ref="{}title"/>
 *         &lt;element ref="{}author" maxOccurs="unbounded"/>
 *         &lt;element ref="{}year"/>
 *         &lt;element ref="{}price"/>
 *       &lt;/sequence>
 *       &lt;attribute name="category" use="required" type="{http://www.w3.org/2001/XMLSchema}string" />
 *       &lt;attribute name="cover" type="{http://www.w3.org/2001/XMLSchema}string" />
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
    "title",
    "author",
    "year",
    "price"
})
@XmlRootElement(name = "book")
@Generated(value = "com.sun.tools.internal.xjc.Driver", date = "2017-06-06T10:59:25-05:00", comments = "JAXB RI v2.2.8-b130911.1802")
public class Book {

    @XmlElement(required = true)
    @Generated(value = "com.sun.tools.internal.xjc.Driver", date = "2017-06-06T10:59:25-05:00", comments = "JAXB RI v2.2.8-b130911.1802")
    protected Title title;
    @XmlElement(required = true)
    @Generated(value = "com.sun.tools.internal.xjc.Driver", date = "2017-06-06T10:59:25-05:00", comments = "JAXB RI v2.2.8-b130911.1802")
    protected List<String> author;
    @XmlElement(required = true)
    @Generated(value = "com.sun.tools.internal.xjc.Driver", date = "2017-06-06T10:59:25-05:00", comments = "JAXB RI v2.2.8-b130911.1802")
    protected BigInteger year;
    @XmlElement(required = true)
    @Generated(value = "com.sun.tools.internal.xjc.Driver", date = "2017-06-06T10:59:25-05:00", comments = "JAXB RI v2.2.8-b130911.1802")
    protected BigDecimal price;
    @XmlAttribute(name = "category", required = true)
    @Generated(value = "com.sun.tools.internal.xjc.Driver", date = "2017-06-06T10:59:25-05:00", comments = "JAXB RI v2.2.8-b130911.1802")
    protected String category;
    @XmlAttribute(name = "cover")
    @Generated(value = "com.sun.tools.internal.xjc.Driver", date = "2017-06-06T10:59:25-05:00", comments = "JAXB RI v2.2.8-b130911.1802")
    protected String cover;

    /**
     * Gets the value of the title property.
     * 
     * @return
     *     possible object is
     *     {@link Title }
     *     
     */
    @Generated(value = "com.sun.tools.internal.xjc.Driver", date = "2017-06-06T10:59:25-05:00", comments = "JAXB RI v2.2.8-b130911.1802")
    public Title getTitle() {
        return title;
    }

    /**
     * Sets the value of the title property.
     * 
     * @param value
     *     allowed object is
     *     {@link Title }
     *     
     */
    @Generated(value = "com.sun.tools.internal.xjc.Driver", date = "2017-06-06T10:59:25-05:00", comments = "JAXB RI v2.2.8-b130911.1802")
    public void setTitle(Title value) {
        this.title = value;
    }

    /**
     * Gets the value of the author property.
     * 
     * <p>
     * This accessor method returns a reference to the live list,
     * not a snapshot. Therefore any modification you make to the
     * returned list will be present inside the JAXB object.
     * This is why there is not a <CODE>set</CODE> method for the author property.
     * 
     * <p>
     * For example, to add a new item, do as follows:
     * <pre>
     *    getAuthor().add(newItem);
     * </pre>
     * 
     * 
     * <p>
     * Objects of the following type(s) are allowed in the list
     * {@link String }
     * 
     * 
     */
    @Generated(value = "com.sun.tools.internal.xjc.Driver", date = "2017-06-06T10:59:25-05:00", comments = "JAXB RI v2.2.8-b130911.1802")
    public List<String> getAuthor() {
        if (author == null) {
            author = new ArrayList<String>();
        }
        return this.author;
    }

    /**
     * Gets the value of the year property.
     * 
     * @return
     *     possible object is
     *     {@link BigInteger }
     *     
     */
    @Generated(value = "com.sun.tools.internal.xjc.Driver", date = "2017-06-06T10:59:25-05:00", comments = "JAXB RI v2.2.8-b130911.1802")
    public BigInteger getYear() {
        return year;
    }

    /**
     * Sets the value of the year property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigInteger }
     *     
     */
    @Generated(value = "com.sun.tools.internal.xjc.Driver", date = "2017-06-06T10:59:25-05:00", comments = "JAXB RI v2.2.8-b130911.1802")
    public void setYear(BigInteger value) {
        this.year = value;
    }

    /**
     * Gets the value of the price property.
     * 
     * @return
     *     possible object is
     *     {@link BigDecimal }
     *     
     */
    @Generated(value = "com.sun.tools.internal.xjc.Driver", date = "2017-06-06T10:59:25-05:00", comments = "JAXB RI v2.2.8-b130911.1802")
    public BigDecimal getPrice() {
        return price;
    }

    /**
     * Sets the value of the price property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigDecimal }
     *     
     */
    @Generated(value = "com.sun.tools.internal.xjc.Driver", date = "2017-06-06T10:59:25-05:00", comments = "JAXB RI v2.2.8-b130911.1802")
    public void setPrice(BigDecimal value) {
        this.price = value;
    }

    /**
     * Gets the value of the category property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    @Generated(value = "com.sun.tools.internal.xjc.Driver", date = "2017-06-06T10:59:25-05:00", comments = "JAXB RI v2.2.8-b130911.1802")
    public String getCategory() {
        return category;
    }

    /**
     * Sets the value of the category property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    @Generated(value = "com.sun.tools.internal.xjc.Driver", date = "2017-06-06T10:59:25-05:00", comments = "JAXB RI v2.2.8-b130911.1802")
    public void setCategory(String value) {
        this.category = value;
    }

    /**
     * Gets the value of the cover property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    @Generated(value = "com.sun.tools.internal.xjc.Driver", date = "2017-06-06T10:59:25-05:00", comments = "JAXB RI v2.2.8-b130911.1802")
    public String getCover() {
        return cover;
    }

    /**
     * Sets the value of the cover property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    @Generated(value = "com.sun.tools.internal.xjc.Driver", date = "2017-06-06T10:59:25-05:00", comments = "JAXB RI v2.2.8-b130911.1802")
    public void setCover(String value) {
        this.cover = value;
    }

}
