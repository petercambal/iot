/**
 * Main configuration file for require.js
 */
require.config({
    paths: {
        jquery: 'lib/jquery-2.1.3.min',
        bootstrap: 'lib/bootstrap.min',
        utils: 'utils'
    },
    shim: {
        bootstrap: ['jquery']
    }
});
