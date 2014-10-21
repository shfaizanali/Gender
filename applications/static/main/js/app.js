(function() {
  var init, module;

  module = angular.module('gender', ['controllers', 'models', 'services']);

  module.config([
    '$routeProvider', '$httpProvider', '$interpolateProvider', function($routeProvider, $httpProvider, $interpolateProvider) {

      $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

      $interpolateProvider.startSymbol('{$');
      $interpolateProvider.endSymbol('$}');

      $routeProvider.when('/help', {
            templateUrl: '/help'
            , controller: 'HelpController'
      });

      $routeProvider.when('/home', {
            templateUrl: '/home'
            , controller: 'HomeController'
      });

      $routeProvider.when('/', {
            templateUrl: '/home'
            , controller: 'HomeController'
      });


      $routeProvider.when('/home', {
            templateUrl: '/home'
            , controller: 'HomeController'
      });

      $routeProvider.when('/signup', {
            templateUrl: '/account/signup/'
            , controller: 'SignupController'
      });

      $routeProvider.when('/login', {
            templateUrl: '/account/login/'
            , controller: 'LoginController'
      });

      $routeProvider.when('/success', {
            templateUrl: '/success/'
            , controller: 'SuccessController'
      });

      $routeProvider.when('/profile', {
            templateUrl: '/profile/'
            , controller: 'ProfileController'
      });

      //$routeProvider.otherwise({
        //redirectTo: '/home'
      //});

    }
  ]);

  module.run([
    '$rootScope', '$http', function($rootScope, $http) {

    }
  ]);

  init = function() {
    return angular.bootstrap(document, ['gender']);
  };

  angular.element(document).ready(init);

}).call(this);
