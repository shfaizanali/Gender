(function() {
  var init, module;

  module = angular.module('gender', ['controllers', 'models', 'services']);


  module.config([
    '$routeProvider', '$httpProvider', '$sceDelegateProvider', function($routeProvider, $httpProvider) {

      $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';


      $routeProvider.when('/help', {
            templateUrl: '/help'
            , controller: 'HelpController'
      });

      $routeProvider.when('/home', {
            templateUrl: '/home'
            , controller: 'HomeController'
      });

      $routeProvider.when('/signup', {
            templateUrl: '/account/signup/'
            , controller: 'SignupController'
      });

      $routeProvider.otherwise({
        redirectTo: '/home'
      });

    }
  ]);

  module.run([
    '$rootScope', function($rootScope, WS_URL) {

    }
  ]);

  init = function() {
    return angular.bootstrap(document, ['gender']);
  };

  angular.element(document).ready(init);

}).call(this);
