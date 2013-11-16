
class sql {
  class {'mysql::server':
  }

  mysql_database { 'pyramid-db':
    ensure => present,
  }

  mysql::user { 'pyramid' :
    ensure => present,
    require  => Service['mysql'],
    password => 'pyramid',
    host     => 'localhost'
  }

  mysql::rights::standard { 'pyramid' :
    database => 'pyramid-db',
    user     => 'pyramid',
    host     => 'localhost',
  }

  mysql_database { 'django-db':
    ensure => present,
  }

  mysql::user { 'django' :
    ensure => present,
    require  => Service['mysql'],
    password => 'django',
    host     => 'localhost'
  }

  mysql::rights::standard { 'django' :
    database => 'django-db',
    user     => 'django',
    host     => 'localhost',
  }
}