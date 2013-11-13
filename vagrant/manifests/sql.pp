
class sql {

  exec { "apt-update-repo":
    command => "/usr/bin/apt-get -y update"
  }

  package {
    ["mysql-client", "mysql-server", "libmysqlclient-dev"]:
      ensure => installed,
      require => Exec['apt-update']
  }

  service { "mysql":
    ensure    => running,
    enable    => true,
    require => Package["mysql-server"],
  }

}