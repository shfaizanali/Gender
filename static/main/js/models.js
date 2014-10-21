(function() {
  var module;

  module = angular.module('models', ['angularFileUpload']);

  module.factory('AuthModel', [
    '$rootScope', '$upload', function($rootScope, $upload) {
        var factory = {};

        return factory;
    }
  ]);

  module.factory('HelpModel', [
    '$rootScope', function($rootScope) {
      
    }
  ]);

}).call(this);
