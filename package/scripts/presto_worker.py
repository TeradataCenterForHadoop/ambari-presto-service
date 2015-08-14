from resource_management import *
import socket

class Worker(Script):
    def install(self, env):
        Execute('wget sdvl3bdch001.td.teradata.com/RPMs/presto-server-rpm-0.114.rpm -P /tmp')
        Execute('rpm -i /tmp/presto-server-rpm-0.114.rpm')
        self.configure(env)

    def stop(self, env):
        Execute('/etc/init.d/presto stop')

    def start(self, env):
        Execute('/etc/init.d/presto start')

    def status(self, env):
        Execute('/etc/init.d/presto status')


    def configure(self, env):
        import params
        key_val_template = '{0}={1}\n'
        with open('/etc/presto/node.properties', 'w') as f:
            for key, value in params.node_properties.iteritems():
                f.write(key_val_template.format(key, value))
            f.write(key_val_template.format('node.id', socket.gethostname()))

        with open('/etc/presto/jvm.config', 'w') as f:
            f.write(params.jvm_config['jvm.config'])

        with open('/etc/presto/config.properties', 'w') as f:
            for key, value in params.config_properties.iteritems():
                if key == 'query.queue-config-file' and value.strip() == '':
                    continue
                f.write(key_val_template.format(key, value))
            f.write(key_val_template.format('coordinator', 'false'))

if __name__ == "__main__":
    Worker().execute()
