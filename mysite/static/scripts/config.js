/**
 * Main configuration file for require.js
 */
require.config({
    paths: {
        jquery: 'lib/jquery-2.1.3.min',
        bootstrap: 'lib/bootstrap.min'
        //treeview: 'lib/bootstrap-treeview',
        //chosen: 'lib/chosen.jquery',
        //underscore: 'lib/underscore.min',
        //datatables: 'lib/jquery.dataTables.min',
        //datatablesBootstrap: 'lib/dataTables.bootstrap',
        //datatablesTableTools: 'lib/dataTables.tableTools.min',
        //datatablesEditable: 'lib/dataTables.editable',
        //holder: 'lib/holder',
        //ie10Viewport: 'lib/ie10-viewport-bug-workaround.js',
        //utils: 'lib/utils',
        //slider: 'lib/bootstrap-slider',
        //switch: 'lib/bootstrap-switch.min',
        //jeditable: 'lib/jeditable'
        //widget: 'lib/jquery.ui.widget',
        //iframeTransport: 'lib/jquery.iframe-transport',
        //fileUpload: 'lib/jquery.fileupload'

    },
    shim: {
        bootstrap: ['jquery']
        //datatables: ['jquery'],
        //datatablesEditable: ['datatables'],
        //chosen: ['jquery'],
        //slider: ['jquery'],
        //switch: ['jquery'],
        //treeview: ['jquery'],
        //jeditable: ['jquery']
        //widget: ['jquery'],
        //iframeTransport: ['jquery'],
        //fileUpload: ['jquery']
    }
});
