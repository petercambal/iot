/**
 * Main configuration file for require.js
 */
require.config({
    paths: {
        jquery: 'lib/jquery-2.1.3.min',
        bootstrap: 'lib/bootstrap.min',
        jqueryui: 'lib/jquery-ui.min',
        treeview: 'lib/bootstrap-treeview',
        datatables: 'lib/jquery.dataTables.min',
        datatablesBootstrap: 'lib/dataTables.bootstrap',
        datatablesTableTools: 'lib/dataTables.tableTools.min',
        chosen: 'lib/chosen.jquery',
        editable : 'lib/bootstrap-editable.min',
        mqtt: 'lib/mqttws31',
        chart: 'lib/Chart.min',
        utils: 'utils',
    },
    shim: {
        bootstrap: ['jquery'],
        jqueryui: ['jquery'],
        datatables: ['jquery'],
        datatablesBootstrap: ['jquery'],
        datatablesTableTools: ['jquery'],
        treeview: ['jquery'],
        chosen: ['jquery'],
        editable: ['jquery'],
        chart: ['jquery']
    }
});
