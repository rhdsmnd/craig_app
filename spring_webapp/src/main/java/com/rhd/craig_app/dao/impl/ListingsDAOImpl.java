package rhd.craig_app.dao.impl;

import rhd.craig_app.dao.ListingsDAO;

import rhd.craig_app.domain.Listing;

import org.springframework.stereotype.Repository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;

import javax.sql.DataSource;

@Repository
public class ListingsDAOImpl implements ListingsDAO {

    private JdbcTemplate jdbcTemplate;

    public Listing[] queryDb(int num) {
        return new Listing[1];
    }

    public JdbcTemplate getJdbcTemplate() {
        return this.jdbcTemplate;
    }
    public void setJdbcTemplate(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    @Autowired
    public void setDataSource(DataSource dataSource) {
        this.jdbcTemplate = new JdbcTemplate(dataSource);
    }

}