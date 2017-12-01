package com.rhd.craig_app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import org.springframework.context.annotation.Bean;

import org.apache.commons.dbcp.BasicDataSource;

import org.springframework.boot.autoconfigure.jdbc.DataSourceBuilder;

import javax.sql.DataSource;

@SpringBootApplication
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @Bean
    public DataSource getDataSource() {
        return DataSourceBuilder.create()
                .url("jdbc:postgresql://localhost/craig_app")
                .username("craig_user")
                .password("asdf")
                .build();
    }

}
