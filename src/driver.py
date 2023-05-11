from cloudshell.shell.core.driver_context import AutoLoadCommandContext, AutoLoadDetails
from cloudshell.shell.core.driver_utils import GlobalLock
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.session.logging_session import LoggingSessionContext
from cloudshell.shell.core.session.cloudshell_session import CloudShellSessionContext
from cloudshell.shell.standards.networking.autoload_model import NetworkingResourceModel
from cloudshell.shell.standards.networking.driver_interface import (
    NetworkingResourceDriverInterface,
)
from cloudshell.shell.standards.networking.resource_config import (
    NetworkingResourceConfig,
)


class DutShell2GDriver(ResourceDriverInterface, NetworkingResourceDriverInterface):
    SHELL_NAME = "DutShell2G"

    def __init__(self):
        pass

    def initialize(self, context):
        pass

    def restore(
        self,
        context,
        path,
        configuration_type,
        restore_method,
        vrf_management_name,
    ):
        pass

    def save(
        self,
        context,
        folder_path,
        configuration_type,
        vrf_management_name,
    ):
        pass

    def load_firmware(self, context, path, vrf_management_name):
        pass

    def run_custom_command(self, context, custom_command):
        pass

    def run_custom_config_command(self, context, custom_command):
        pass

    def shutdown(self, context):
        pass

    def orchestration_save(self, context, mode, custom_params):
        pass

    def orchestration_restore(self, context, saved_artifact_info, custom_params):
        pass

    def ApplyConnectivityChanges(self, context, request):
        pass

    @GlobalLock.lock
    def get_inventory(self, context: AutoLoadCommandContext) -> AutoLoadDetails:
        """Create a resource structure."""
        with LoggingSessionContext(context):
            api = CloudShellSessionContext(context).get_api()
            resource_config = NetworkingResourceConfig.from_context(context, api)
            resource_model = NetworkingResourceModel.from_resource_config(
                resource_config
            )
            resource_model.system_name = "DUT device"

            chassis1 = resource_model.entities.Chassis(index=1)
            resource_model.connect_chassis(chassis1)

            module1 = resource_model.entities.Module(index=1)
            chassis1.connect_module(module1)

            port1 = resource_model.entities.Port(index=1)
            port2 = resource_model.entities.Port(index=2)
            module1.connect_port(port1)
            module1.connect_port(port2)

        return resource_model.build()

    def health_check(self, cancellation_context):
        pass

    def cleanup(self):
        pass
