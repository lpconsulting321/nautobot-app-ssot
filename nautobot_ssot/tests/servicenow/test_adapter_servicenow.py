"""Unit tests for the ServiceNowDiffSync adapter class."""

import uuid

from django.contrib.contenttypes.models import ContentType

from nautobot.extras.models import Job, JobResult
from nautobot.utilities.testing import TransactionTestCase

from nautobot_ssot.integrations.servicenow.jobs import ServiceNowDataTarget
from nautobot_ssot.integrations.servicenow.diffsync.adapter_servicenow import ServiceNowDiffSync


class MockServiceNowClient:
    """Mock version of the ServiceNowClient class using canned data."""

    def get_by_sys_id(self, table, sys_id):  # pylint: disable=unused-argument,no-self-use
        """Get a record with a given sys_id from a given table."""
        return None

    def all_table_entries(self, table, query=None):
        """Iterator over all records in a given table."""

        if table == "cmn_location":
            yield from [
                {
                    "country": "",
                    "parent": "",
                    "city": "",
                    "latitude": "",
                    "sys_updated_on": "2021-07-12 20:19:23",
                    "sys_id": "7200ad3d2f153010fe08351ef699b69a",
                    "sys_updated_by": "admin",
                    "stock_room": "false",
                    "street": "",
                    "sys_created_on": "2021-07-12 20:19:23",
                    "contact": "",
                    "phone_territory": "",
                    "company": "",
                    "lat_long_error": "",
                    "state": "",
                    "sys_created_by": "admin",
                    "longitude": "",
                    "zip": "",
                    "sys_mod_count": "0",
                    "sys_tags": "",
                    "time_zone": "",
                    "full_name": "Asia",
                    "fax_phone": "",
                    "phone": "",
                    "name": "Asia",
                    "coordinates_retrieved_on": "",
                },
                {
                    "country": "Japan",
                    "parent": "7200ad3d2f153010fe08351ef699b69a",
                    "city": "Japan",
                    "latitude": "36.204824",
                    "sys_updated_on": "2021-07-12 20:19:30",
                    "sys_id": "0d9561b437d0200044e0bfc8bcbe5d32",
                    "sys_updated_by": "admin",
                    "stock_room": "false",
                    "street": "",
                    "sys_created_on": "2012-02-17 17:57:16",
                    "contact": "",
                    "phone_territory": "dcb7e002eb1201007128a5fc5206fe64",
                    "company": "81fd65ecac1d55eb42a426568fc87a63",
                    "lat_long_error": "",
                    "state": "",
                    "sys_created_by": "admin",
                    "longitude": "138.252924",
                    "zip": "",
                    "sys_mod_count": "1",
                    "sys_tags": "",
                    "time_zone": "",
                    "full_name": "Asia/Japan",
                    "fax_phone": "",
                    "phone": "",
                    "name": "Japan",
                    "coordinates_retrieved_on": "",
                },
                {
                    "country": "Japan",
                    "parent": "0d9561b437d0200044e0bfc8bcbe5d32",
                    "city": "Tokyo",
                    "latitude": "35.6894875",
                    "sys_updated_on": "2012-02-19 17:11:11",
                    "sys_id": "821c169bac1d55eb68ede6e36aa35112",
                    "sys_updated_by": "admin",
                    "stock_room": "false",
                    "street": "",
                    "sys_created_on": "2010-11-25 08:17:47",
                    "contact": "",
                    "phone_territory": "",
                    "company": "81fd65ecac1d55eb42a426568fc87a63",
                    "lat_long_error": "",
                    "state": "",
                    "sys_created_by": "dariusz.maint",
                    "longitude": "139.6917064",
                    "zip": "",
                    "sys_mod_count": "3",
                    "sys_tags": "",
                    "time_zone": "",
                    "full_name": "Asia/Japan/Tokyo",
                    "fax_phone": "",
                    "phone": "",
                    "name": "Tokyo",
                    "coordinates_retrieved_on": "",
                },
                {
                    "country": "China",
                    "parent": "7200ad3d2f153010fe08351ef699b69a",
                    "city": "China",
                    "latitude": "35.86166",
                    "sys_updated_on": "2021-07-12 20:19:26",
                    "sys_id": "8195ad7437d0200044e0bfc8bcbe5d8f",
                    "sys_updated_by": "admin",
                    "stock_room": "false",
                    "street": "",
                    "sys_created_on": "2012-02-17 17:57:15",
                    "contact": "",
                    "phone_territory": "4cb7e002eb1201007128a5fc5206fe0b",
                    "company": "81fdf9ebac1d55eb4cb89f136a082555",
                    "lat_long_error": "",
                    "state": "",
                    "sys_created_by": "admin",
                    "longitude": "104.195397",
                    "zip": "",
                    "sys_mod_count": "1",
                    "sys_tags": "",
                    "time_zone": "",
                    "full_name": "Asia/China",
                    "fax_phone": "",
                    "phone": "",
                    "name": "China",
                    "coordinates_retrieved_on": "",
                },
                {
                    "country": "",
                    "parent": "8195ad7437d0200044e0bfc8bcbe5d8f",
                    "city": "",
                    "latitude": "",
                    "sys_updated_on": "2021-07-14 21:39:47",
                    "sys_id": "84a54c662f513010fe08351ef699b624",
                    "sys_updated_by": "admin",
                    "stock_room": "false",
                    "street": "",
                    "sys_created_on": "2021-07-14 21:39:47",
                    "contact": "",
                    "phone_territory": "",
                    "company": "",
                    "lat_long_error": "",
                    "state": "",
                    "sys_created_by": "admin",
                    "longitude": "",
                    "zip": "",
                    "sys_mod_count": "0",
                    "sys_tags": "",
                    "time_zone": "",
                    "full_name": "Asia/China/hkg",
                    "fax_phone": "",
                    "phone": "",
                    "name": "hkg",
                    "coordinates_retrieved_on": "",
                },
            ]
        elif table == "cmdb_ci_ip_switch":
            if query and query["location"] == "84a54c662f513010fe08351ef699b624":  # hkg
                yield from [
                    {
                        "attested_date": "",
                        "can_switch": "false",
                        "stack": "false",
                        "operational_status": "1",
                        "cpu_manufacturer": "",
                        "sys_updated_on": "2021-07-14 21:45:09",
                        "discovery_source": "",
                        "first_discovered": "",
                        "due_in": "",
                        "can_partitionvlans": "false",
                        "gl_account": "",
                        "invoice_number": "",
                        "sys_created_by": "admin",
                        "ram": "",
                        "warranty_expiration": "",
                        "cpu_speed": "",
                        "owned_by": "",
                        "checked_out": "",
                        "firmware_manufacturer": "",
                        "disk_space": "",
                        "sys_domain_path": "/",
                        "discovery_proto_id": "",
                        "maintenance_schedule": "",
                        "cost_center": "",
                        "attested_by": "",
                        "dns_domain": "",
                        "assigned": "",
                        "life_cycle_stage": "",
                        "purchase_date": "",
                        "short_description": "",
                        "managed_by": "",
                        "range": "",
                        "firmware_version": "",
                        "can_print": "false",
                        "last_discovered": "",
                        "ports": "",
                        "sys_class_name": "cmdb_ci_ip_switch",
                        "cpu_count": "1",
                        "manufacturer": "",
                        "life_cycle_stage_status": "",
                        "vendor": "",
                        "can_route": "false",
                        "model_number": "",
                        "assigned_to": "",
                        "start_date": "",
                        "bandwidth": "",
                        "serial_number": "",
                        "support_group": "",
                        "correlation_id": "",
                        "unverified": "false",
                        "attributes": "",
                        "asset": "a2d60ce62f513010fe08351ef699b618",
                        "skip_sync": "false",
                        "device_type": "",
                        "attestation_score": "",
                        "sys_updated_by": "admin",
                        "sys_created_on": "2021-07-14 21:40:27",
                        "cpu_type": "",
                        "sys_domain": "global",
                        "install_date": "",
                        "asset_tag": "",
                        "hardware_substatus": "",
                        "fqdn": "",
                        "stack_mode": "",
                        "change_control": "",
                        "internet_facing": "true",
                        "physical_interface_count": "",
                        "delivery_date": "",
                        "hardware_status": "installed",
                        "channels": "",
                        "install_status": "1",
                        "supported_by": "",
                        "name": "hkg-leaf-01",
                        "subcategory": "IP",
                        "default_gateway": "",
                        "assignment_group": "",
                        "managed_by_group": "",
                        "can_hub": "false",
                        "sys_id": "f9c500a62f513010fe08351ef699b65b",
                        "po_number": "",
                        "checked_in": "",
                        "sys_class_path": "/!!/!2/!!/!,",
                        "mac_address": "",
                        "company": "",
                        "justification": "",
                        "department": "",
                        "snmp_sys_location": "",
                        "comments": "",
                        "cost": "",
                        "sys_mod_count": "1",
                        "monitor": "false",
                        "ip_address": "",
                        "model_id": "aa722dbd2f153010fe08351ef699b605",
                        "duplicate_of": "",
                        "sys_tags": "",
                        "cost_cc": "USD",
                        "discovery_proto_type": "",
                        "order_date": "",
                        "schedule": "",
                        "environment": "",
                        "due": "",
                        "attested": "false",
                        "location": "84a54c662f513010fe08351ef699b624",
                        "category": "Resource",
                        "fault_count": "0",
                        "lease_id": "",
                    },
                    {
                        "attested_date": "",
                        "can_switch": "false",
                        "stack": "false",
                        "operational_status": "1",
                        "cpu_manufacturer": "",
                        "sys_updated_on": "2021-07-14 21:45:07",
                        "discovery_source": "",
                        "first_discovered": "",
                        "due_in": "",
                        "can_partitionvlans": "false",
                        "gl_account": "",
                        "invoice_number": "",
                        "sys_created_by": "admin",
                        "ram": "",
                        "warranty_expiration": "",
                        "cpu_speed": "",
                        "owned_by": "",
                        "checked_out": "",
                        "firmware_manufacturer": "",
                        "disk_space": "",
                        "sys_domain_path": "/",
                        "discovery_proto_id": "",
                        "maintenance_schedule": "",
                        "cost_center": "",
                        "attested_by": "",
                        "dns_domain": "",
                        "assigned": "",
                        "life_cycle_stage": "",
                        "purchase_date": "",
                        "short_description": "",
                        "managed_by": "",
                        "range": "",
                        "firmware_version": "",
                        "can_print": "false",
                        "last_discovered": "",
                        "ports": "",
                        "sys_class_name": "cmdb_ci_ip_switch",
                        "cpu_count": "1",
                        "manufacturer": "",
                        "life_cycle_stage_status": "",
                        "vendor": "",
                        "can_route": "false",
                        "model_number": "",
                        "assigned_to": "",
                        "start_date": "",
                        "bandwidth": "",
                        "serial_number": "",
                        "support_group": "",
                        "correlation_id": "",
                        "unverified": "false",
                        "attributes": "",
                        "asset": "9ed6c8e62f513010fe08351ef699b6c8",
                        "skip_sync": "false",
                        "device_type": "",
                        "attestation_score": "",
                        "sys_updated_by": "admin",
                        "sys_created_on": "2021-07-14 21:40:36",
                        "cpu_type": "",
                        "sys_domain": "global",
                        "install_date": "",
                        "asset_tag": "",
                        "hardware_substatus": "",
                        "fqdn": "",
                        "stack_mode": "",
                        "change_control": "",
                        "internet_facing": "true",
                        "physical_interface_count": "",
                        "delivery_date": "",
                        "hardware_status": "installed",
                        "channels": "",
                        "install_status": "1",
                        "supported_by": "",
                        "name": "hkg-leaf-02",
                        "subcategory": "IP",
                        "default_gateway": "",
                        "assignment_group": "",
                        "managed_by_group": "",
                        "can_hub": "false",
                        "sys_id": "c4d540a62f513010fe08351ef699b602",
                        "po_number": "",
                        "checked_in": "",
                        "sys_class_path": "/!!/!2/!!/!,",
                        "mac_address": "",
                        "company": "",
                        "justification": "",
                        "department": "",
                        "snmp_sys_location": "",
                        "comments": "",
                        "cost": "",
                        "sys_mod_count": "1",
                        "monitor": "false",
                        "ip_address": "",
                        "model_id": "aa722dbd2f153010fe08351ef699b605",
                        "duplicate_of": "",
                        "sys_tags": "",
                        "cost_cc": "USD",
                        "discovery_proto_type": "",
                        "order_date": "",
                        "schedule": "",
                        "environment": "",
                        "due": "",
                        "attested": "false",
                        "location": "84a54c662f513010fe08351ef699b624",
                        "category": "Resource",
                        "fault_count": "0",
                        "lease_id": "",
                    },
                ]
            else:
                yield from []
        elif table == "cmdb_ci_network_adapter":
            if query and query["cmdb_ci"] == "f9c500a62f513010fe08351ef699b65b":  # hkg-leaf-01
                yield from [
                    {
                        "mac_manufacturer": "",
                        "attested_date": "",
                        "skip_sync": "false",
                        "operational_status": "1",
                        "sys_updated_on": "2021-07-14 21:40:27",
                        "attestation_score": "",
                        "discovery_source": "",
                        "first_discovered": "",
                        "sys_updated_by": "admin",
                        "due_in": "",
                        "sys_created_on": "2021-07-14 21:40:27",
                        "sys_domain": "global",
                        "install_date": "",
                        "gl_account": "",
                        "invoice_number": "",
                        "sys_created_by": "admin",
                        "warranty_expiration": "",
                        "asset_tag": "",
                        "cmdb_ci": "f9c500a62f513010fe08351ef699b65b",
                        "fqdn": "",
                        "change_control": "",
                        "owned_by": "",
                        "checked_out": "",
                        "sys_domain_path": "/",
                        "dhcp_enabled": "false",
                        "delivery_date": "",
                        "maintenance_schedule": "",
                        "install_status": "1",
                        "cost_center": "",
                        "attested_by": "",
                        "supported_by": "",
                        "dns_domain": "",
                        "name": "Ethernet1",
                        "assigned": "",
                        "life_cycle_stage": "",
                        "purchase_date": "",
                        "subcategory": "Network",
                        "short_description": "",
                        "virtual": "false",
                        "assignment_group": "",
                        "managed_by": "",
                        "managed_by_group": "",
                        "can_print": "false",
                        "last_discovered": "",
                        "sys_class_name": "cmdb_ci_network_adapter",
                        "manufacturer": "",
                        "sys_id": "f9c500a62f513010fe08351ef699b65d",
                        "po_number": "",
                        "checked_in": "",
                        "netmask": "255.255.255.0",
                        "sys_class_path": "/!!/!8",
                        "life_cycle_stage_status": "",
                        "mac_address": "",
                        "vendor": "",
                        "alias": "",
                        "company": "",
                        "justification": "",
                        "model_number": "",
                        "department": "",
                        "assigned_to": "",
                        "start_date": "",
                        "comments": "",
                        "cost": "",
                        "sys_mod_count": "0",
                        "monitor": "false",
                        "serial_number": "",
                        "ip_address": "",
                        "model_id": "",
                        "duplicate_of": "",
                        "sys_tags": "",
                        "cost_cc": "USD",
                        "order_date": "",
                        "schedule": "",
                        "support_group": "",
                        "environment": "",
                        "due": "",
                        "attested": "false",
                        "correlation_id": "",
                        "unverified": "false",
                        "attributes": "",
                        "location": "",
                        "asset": "",
                        "category": "Hardware",
                        "fault_count": "0",
                        "ip_default_gateway": "",
                        "lease_id": "",
                    },
                    {
                        "mac_manufacturer": "",
                        "attested_date": "",
                        "skip_sync": "false",
                        "operational_status": "1",
                        "sys_updated_on": "2021-07-14 21:40:28",
                        "attestation_score": "",
                        "discovery_source": "",
                        "first_discovered": "",
                        "sys_updated_by": "admin",
                        "due_in": "",
                        "sys_created_on": "2021-07-14 21:40:28",
                        "sys_domain": "global",
                        "install_date": "",
                        "gl_account": "",
                        "invoice_number": "",
                        "sys_created_by": "admin",
                        "warranty_expiration": "",
                        "asset_tag": "",
                        "cmdb_ci": "f9c500a62f513010fe08351ef699b65b",
                        "fqdn": "",
                        "change_control": "",
                        "owned_by": "",
                        "checked_out": "",
                        "sys_domain_path": "/",
                        "dhcp_enabled": "false",
                        "delivery_date": "",
                        "maintenance_schedule": "",
                        "install_status": "1",
                        "cost_center": "",
                        "attested_by": "",
                        "supported_by": "",
                        "dns_domain": "",
                        "name": "Ethernet2",
                        "assigned": "",
                        "life_cycle_stage": "",
                        "purchase_date": "",
                        "subcategory": "Network",
                        "short_description": "",
                        "virtual": "false",
                        "assignment_group": "",
                        "managed_by": "",
                        "managed_by_group": "",
                        "can_print": "false",
                        "last_discovered": "",
                        "sys_class_name": "cmdb_ci_network_adapter",
                        "manufacturer": "",
                        "sys_id": "4ac500a62f513010fe08351ef699b65f",
                        "po_number": "",
                        "checked_in": "",
                        "netmask": "255.255.255.0",
                        "sys_class_path": "/!!/!8",
                        "life_cycle_stage_status": "",
                        "mac_address": "",
                        "vendor": "",
                        "alias": "",
                        "company": "",
                        "justification": "",
                        "model_number": "",
                        "department": "",
                        "assigned_to": "",
                        "start_date": "",
                        "comments": "",
                        "cost": "",
                        "sys_mod_count": "0",
                        "monitor": "false",
                        "serial_number": "",
                        "ip_address": "",
                        "model_id": "",
                        "duplicate_of": "",
                        "sys_tags": "",
                        "cost_cc": "USD",
                        "order_date": "",
                        "schedule": "",
                        "support_group": "",
                        "environment": "",
                        "due": "",
                        "attested": "false",
                        "correlation_id": "",
                        "unverified": "false",
                        "attributes": "",
                        "location": "",
                        "asset": "",
                        "category": "Hardware",
                        "fault_count": "0",
                        "ip_default_gateway": "",
                        "lease_id": "",
                    },
                ]
            else:
                yield from []
        else:
            yield from []


class ServiceNowDiffSyncTestCase(TransactionTestCase):
    """Test the ServiceNowDiffSync adapter class."""

    databases = ("default", "job_logs")

    def test_data_loading(self):
        """Test the load() function."""
        job = ServiceNowDataTarget()
        job.job_result = JobResult.objects.create(
            name=job.class_path, obj_type=ContentType.objects.get_for_model(Job), user=None, job_id=uuid.uuid4()
        )
        snds = ServiceNowDiffSync(job=job, sync=None, client=MockServiceNowClient())
        snds.load()

        self.assertEqual(
            ["Asia", "China", "Japan", "Tokyo", "hkg"],
            sorted(loc.get_unique_id() for loc in snds.get_all("location")),
        )
        japan = snds.get("location", "Japan")
        self.assertEqual("Asia", japan.parent_location_name)
        self.assertEqual("0d9561b437d0200044e0bfc8bcbe5d32", japan.sys_id)
        self.assertEqual([], japan.devices)

        tokyo = snds.get("location", "Tokyo")
        self.assertEqual("Japan", tokyo.parent_location_name)
        self.assertEqual([], tokyo.devices)

        hkg = snds.get("location", "hkg")
        self.assertEqual("China", hkg.parent_location_name)
        self.assertEqual(["hkg-leaf-01", "hkg-leaf-02"], hkg.devices)

        self.assertEqual(
            ["hkg-leaf-01", "hkg-leaf-02"],
            sorted(dev.get_unique_id() for dev in snds.get_all("device")),
        )

        hkg_leaf_01 = snds.get("device", "hkg-leaf-01")
        self.assertEqual("hkg", hkg_leaf_01.location_name)
        self.assertEqual(["hkg-leaf-01__Ethernet1", "hkg-leaf-01__Ethernet2"], hkg_leaf_01.interfaces)

        self.assertEqual(
            ["hkg-leaf-01__Ethernet1", "hkg-leaf-01__Ethernet2"],
            sorted(intf.get_unique_id() for intf in snds.get_all("interface")),
        )
