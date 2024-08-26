# Nautobot Single Source of Truth (SSoT)

<p align="center">
  <img src="https://raw.githubusercontent.com/nautobot/nautobot-app-ssot/develop/docs/images/icon-nautobot-ssot.png" class="logo" height="200px">
  <br>
  <a href="https://github.com/nautobot/nautobot-app-ssot/actions"><img src="https://github.com/nautobot/nautobot-app-ssot/actions/workflows/ci.yml/badge.svg?branch=main"></a>
  <a href="https://docs.nautobot.com/projects/ssot/en/latest/"><img src="https://readthedocs.org/projects/nautobot-plugin-ssot/badge/"></a>
  <a href="https://pypi.org/project/nautobot-ssot/"><img src="https://img.shields.io/pypi/v/nautobot-ssot"></a>
  <a href="https://pypi.org/project/nautobot-ssot/"><img src="https://img.shields.io/pypi/dm/nautobot-ssot"></a>
  <br>
  An <a href="https://networktocode.com/nautobot-apps/">App</a> for <a href="https://nautobot.com/">Nautobot</a>.
</p>


## Overview

An app for [Nautobot](https://github.com/nautobot/nautobot). This Nautobot app facilitates integration and data synchronization between various "source of truth" (SoT) systems, with Nautobot acting as a central clearinghouse for data - a Single Source of Truth, if you will.

The Nautobot SSoT app builds atop the [DiffSync](https://github.com/networktocode/diffsync) Python library and Nautobot's Jobs feature. This enables the rapid development and integration of Jobs that can be run within Nautobot to pull data from other systems ("Data Sources") into Nautobot and/or push data from Nautobot into other systems ("Data Targets") as desired. Key features include the following:

* A dashboard UI lists all registered Data Sources and Data Targets and provides a summary of the synchronization history.
* The outcome of executing of a data synchronization Job is automatically saved to Nautobot's database for later review.
* Detailed logging output generated by DiffSync is automatically captured and saved to the database as well.

### Integrations

This Nautobot application framework includes the following integrations:

- Cisco ACI
- Arista CloudVision
- Device42
- Cisco DNA Center
- Infoblox
- IPFabric
- Itential
- ServiceNow

Read more about integrations [here](https://docs.nautobot.com/projects/ssot/en/latest/user/integrations). To enable and configure integrations follow the instructions from [the install guide](https://docs.nautobot.com/projects/ssot/en/latest/admin/install/#integrations-configuration).

### Screenshots

---

The dashboard view of the app.
![Dashboard View](https://raw.githubusercontent.com/nautobot/nautobot-app-ssot/develop/docs/images/dashboard_initial.png)

---

The detailed view of the example data source that is prepackaged within this app.
![Data Source Detail View](https://raw.githubusercontent.com/nautobot/nautobot-app-ssot/develop/docs/images/data_source_detail.png)

---

The detailed view of an executed sync.
![Sync Detail View](https://raw.githubusercontent.com/nautobot/nautobot-app-ssot/develop/docs/images/sync_detail.png)

---

More screenshots can be found in the [Using the App](https://docs.nautobot.com/projects/ssot/en/latest/user/app_use_cases/) page in the documentation.

## Try it out!

This Nautobot app is installed in the Nautobot Community Sandbox found over at [demo.nautobot.com](https://demo.nautobot.com/)!

> For a full list of all the available always-on sandbox environments, head over to the main page on [networktocode.com](https://www.networktocode.com/nautobot/sandbox-environments/).

## Documentation

Full documentation for this app can be found over on the [Nautobot Docs](https://docs.nautobot.com) website:

* [User Guide](https://docs.nautobot.com/projects/ssot/en/latest/user/app_overview/) - Overview, Using the App, Getting Started, Developing Jobs.
* [Administrator Guide](https://docs.nautobot.com/projects/ssot/en/latest/admin/install/) - How to Install, Configure, Upgrade, or Uninstall the App.
* [Developer Guide](https://docs.nautobot.com/projects/ssot/en/latest/dev/contributing/) - Extending the App, Code Reference, Contribution Guide.
* [Release Notes / Changelog](https://docs.nautobot.com/projects/ssot/en/latest/admin/release_notes/).

## Note On Integration Compatability

The SSoT framework includes a number of integrations with external Systems of Record:

* Cisco ACI
* Arista CloudVision
* Device42
* Cisco DNA Center
* Infoblox
* Itential
* ServiceNow

> Note that the Arista CloudVision integration is currently incompatible with the [Arista Labs](https://labs.arista.com/) environment due to a TLS issue. It has been confirmed to work in on-prem environments previously.

### Contributing to the Documentation

You can find all the Markdown source for the App documentation under the [`docs`](https://github.com/nautobot/nautobot-app-ssot/tree/develop/docs) folder in this repository. For simple edits, a Markdown capable editor is sufficient: clone the repository and edit away.

If you need to view the fully-generated documentation site, you can build it with [MkDocs](https://www.mkdocs.org/). A container hosting the documentation can be started using the `invoke` commands (details in the [Development Environment Guide](https://docs.nautobot.com/projects/ssot/en/latest/dev/dev_environment/#docker-development-environment)) on [http://localhost:8001](http://localhost:8001). Using this container, as your changes to the documentation are saved, they will be automatically rebuilt and any pages currently being viewed will be reloaded in your browser.

Any PRs with fixes or improvements are very welcome!

## Questions

For any questions or comments, please check the [FAQ](https://docs.nautobot.com/projects/ssot/en/latest/user/faq/) first. Feel free to also swing by the [Network to Code Slack](https://networktocode.slack.com/) (channel `#nautobot`), sign up [here](http://slack.networktocode.com/) if you don't have an account.

## Acknowledgements

This project includes code originally written in separate Nautobot apps, which have been merged into this project:

- [nautobot-plugin-ssot-aci](https://github.com/nautobot/nautobot-plugin-ssot-aci):
    Thanks
    [@chadell](https://github.com/chadell),
    [@dnewood](https://github.com/dnewood),
    [@progala](https://github.com/progala),
    [@ubajze](https://github.com/ubajze)
- [nautobot-plugin-ssot-arista-cloudvision](https://github.com/nautobot/nautobot-plugin-ssot-arista-cloudvision):
    Thanks
    [@burnyd](https://github.com/burnyd),
    [@chipn](https://github.com/chipn),
    [@jdrew82](https://github.com/jdrew82),
    [@jvanderaa](https://github.com/jvanderaa),
    [@nniehoff](https://github.com/nniehoff),
    [@qduk](https://github.com/qduk),
    [@ubajze](https://github.com/ubajze)
- [nautobot-plugin-ssot-device42](https://github.com/nautobot/nautobot-plugin-ssot-device42):
    Thanks
    [@jdrew82](https://github.com/jdrew82)
- [nautobot-plugin-ssot-dna-center](https://github.com/nautobot/nautobot-plugin-ssot-dna-center):
    Thanks
    [@jdrew82](https://github.com/jdrew82)
- [nautobot-plugin-ssot-infoblox](https://github.com/nautobot/nautobot-plugin-ssot-infoblox):
    Thanks
    [@FragmentedPacket](https://github.com/FragmentedPacket),
    [@chadell](https://github.com/chadell),
    [@jdrew82](https://github.com/jdrew82),
    [@jtdub](https://github.com/jtdub),
    [@pke11y](https://github.com/pke11y),
    [@smk4664](https://github.com/smk4664),
    [@ubajze](https://github.com/ubajze)
    [@whitej6](https://github.com/whitej6),
- [nautobot-plugin-ssot-ipfabric](https://github.com/nautobot/nautobot-plugin-ssot-ipfabric):
    Thanks
    [@FragmentedPacket](https://github.com/FragmentedPacket),
    [@armartirosyan](https://github.com/armartirosyan),
    [@chadell](https://github.com/chadell),
    [@grelleum](https://github.com/grelleum),
    [@h4ndzdatm0ld](https://github.com/h4ndzdatm0ld),
    [@jdrew82](https://github.com/jdrew82),
    [@justinjeffery-ipf](https://github.com/justinjeffery-ipf),
    [@pke11y](https://github.com/pke11y),
    [@ubajze](https://github.com/ubajze)
    [@whitej6](https://github.com/whitej6),
- [nautobot-plugin-ssot-servicenow](https://github.com/nautobot/nautobot-plugin-ssot-servicenow):
    Thanks
    [@chadell](https://github.com/chadell),
    [@glennmatthews](https://github.com/glennmatthews),
    [@qduk](https://github.com/qduk),
    [@ubajze](https://github.com/ubajze)
