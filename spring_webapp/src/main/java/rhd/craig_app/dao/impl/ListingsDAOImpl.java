package rhd.craig_app.dao.impl;

import org.springframework.stereotype.Repository;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.jdbc.core.JdbcTemplate;

import javax.sql.DataSource;

@Repository
public class ListingsDAOImpl {

    private JdbcTemplate jdbcTemplate;


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