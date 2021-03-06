package com.rhd.craig_app.domain;

import java.util.Date;
import java.util.List;

public class ListingsParam {
    public enum SortCategory {
        DATE, PRICE, NONE
    }

    public enum SortOrder {
        ASCENDING, DESCENDING
    }

    private SortCategory sortedBy;
    private SortOrder sortOrder;

    private Date beginDate;
    private Date endDate;

    private Double minPrice;
    private Double maxPrice;

    private Short[] bedrooms;

    private String[] neighborhoods;

    private List<Double[]> areasOfInterest;
    private List<Double[]> areasOfDisinterest;

    public com.rhd.craig_app.domain.ListingsParam.SortCategory getSortedBy() {
        return sortedBy;
    }

    public void setSortedBy(com.rhd.craig_app.domain.ListingsParam.SortCategory sortedBy) {
        this.sortedBy = sortedBy;
    }

    public com.rhd.craig_app.domain.ListingsParam.SortOrder getSortOrder() {
        return sortOrder;
    }

    public void setSortOrder(com.rhd.craig_app.domain.ListingsParam.SortOrder sortOrder) {
        this.sortOrder = sortOrder;
    }

    public Date getBeginDate() {
        return beginDate;
    }

    public void setBeginDate(Date beginDate) {
        this.beginDate = beginDate;
    }

    public Date getEndDate() {
        return endDate;
    }

    public void setEndDate(Date endDate) {
        this.endDate = endDate;
    }

    public Double getMinPrice() {
        return minPrice;
    }

    public void setMinPrice(Double minPrice) {
        this.minPrice = minPrice;
    }

    public Double getMaxPrice() {
        return maxPrice;
    }

    public void setMaxPrice(Double maxPrice) {
        this.maxPrice = maxPrice;
    }

    public Short[] getBedrooms() {
        return bedrooms;
    }

    public void setBedrooms(Short[] bedrooms) {
        this.bedrooms = bedrooms;
    }

    public String[] getNeighborhoods() {
        return neighborhoods;
    }

    public void setNeighborhoods(String[] neighborhoods) {
        this.neighborhoods = neighborhoods;
    }

    public List<Double[]> getAreasOfInterest() {
        return areasOfInterest;
    }

    public void setAreasOfInterest(List<Double[]> areasOfInterest) {
        this.areasOfInterest = areasOfInterest;
    }

    public List<Double[]> getAreasOfDisinterest() {
        return areasOfDisinterest;
    }

    public void setAreasOfDisinterest(List<Double[]> areasOfDisinterest) {
        this.areasOfDisinterest = areasOfDisinterest;
    }
}