import "sql.pp"

class core {

    exec { "apt-update":
      command => "/usr/bin/sudo apt-get -y update"
    }

    package {
      [ "build-essential" ]:
        ensure => ["installed"],
        require => Exec['apt-update']
    }
}

class python {

    package {
      [ "python", "python-setuptools", "python-dev", "python-pip"]:
        ensure => ["installed"],
        require => Exec['apt-update']
    }

    exec {
      "virtualenv":
      command => "/usr/bin/sudo pip install virtualenv",
      require => Package["python-dev", "python-pip"]
    }

}

class pythondev {
    package {
        [ "dpkg-dev", "swig", "python2.7-dev", "libwebkitgtk-dev", "libjpeg-dev",
          "libtiff4-dev", "checkinstall", "ubuntu-restricted-extras", "freeglut3",
          "freeglut3-dev", "libgtk2.0-dev", "libsdl1.2-dev", "libwxgtk2.8-dev" ]:
        ensure => ["installed"],
        require => Exec['apt-update']
    }
}

class networking {
    package {
      [ "snmp", "tkmib", "curl", "wget" ]:
        ensure => ["installed"],
        require => Exec['apt-update']
    }
}

include core
include python
include pythondev
include networking
include sql
