/*jshint esversion: 6 */

function handle_3d() {
    if (!BABYLON.Engine.isSupported()) {
        dbg("BABYLON is not Supported")
        return
    }
    var ZOOM = 1
    var MAIN_MESH
    
    var canvas = document.getElementById("first-canvas");
    var engine = new BABYLON.Engine(canvas, true);
    var scene = new BABYLON.Scene(engine);
    // set scene background transparent
    scene.clearColor = new BABYLON.Color4(1,0,0,0);
    
    var light = new BABYLON.DirectionalLight("light1", new BABYLON.Vector3(4, -3, 0), scene);
    light.intensity = 3;
    
    var camera = new BABYLON.FreeCamera('camera', new BABYLON.Vector3(-4, 2, 0), scene);
    camera.setTarget(BABYLON.Vector3.Zero());
    camera.attachControl(canvas, false);
    
    BABYLON.SceneLoader.ImportMesh(["Cube",], "/static/quatropack2/models/", "ss.gltf", scene,         
        function (meshes, particleSystems, skeletons) {
            MAIN_MESH = meshes[0]
            engine.runRenderLoop(function() {
                scene.render();
                MAIN_MESH.rotation.y += 0.01
            });
            window.addEventListener("resize", function() {
                engine.resize();
            });
        });

    $('.qp-zoomin').click(function() {
        if (ZOOM > 2) return
        dbg('+')
        dbg(MAIN_MESH.scaling)
        ZOOM += .1
        MAIN_MESH.scaling = new BABYLON.Vector3(ZOOM, ZOOM, -1*ZOOM)
    })
    $('.qp-zoomout').click(function() {
        if (ZOOM < .2) return
        dbg('-')
        ZOOM -= .1
        MAIN_MESH.scaling = new BABYLON.Vector3(ZOOM, ZOOM, -1*ZOOM)
    })
}
    
function handle_3d_2() {
    if (!BABYLON.Engine.isSupported()) {
        dbg("BABYLON is not Supported")
        return
    }
    var ZOOM = 1
    var MAIN_MESH
    
    var canvas = document.getElementById("second-canvas");
    var engine = new BABYLON.Engine(canvas, true);
    var scene = new BABYLON.Scene(engine);
    // set scene background transparent
    scene.clearColor = new BABYLON.Color4(1,0,0,0);
    
    var light = new BABYLON.DirectionalLight("light1", new BABYLON.Vector3(4, -3, 0), scene);
    light.intensity = 3;
    var light2 = new BABYLON.HemisphericLight("light2", new BABYLON.Vector3(0, 1, 0), scene);
    light2.intensity = 0.7;
    
    var camera = new BABYLON.FreeCamera('camera', new BABYLON.Vector3(-4, 2, 0), scene);
    camera.setTarget(BABYLON.Vector3.Zero());
    camera.attachControl(canvas, false);
    
    BABYLON.SceneLoader.ImportMesh(["Cube",], "/static/quatropack2/models/", "ss_75.gltf", scene,         
        function (meshes, particleSystems, skeletons) {
            MAIN_MESH = meshes[0]
            engine.runRenderLoop(function() {
                scene.render();
                MAIN_MESH.rotation.y -= 0.008
            });
            window.addEventListener("resize", function() {
                engine.resize();
            });
        });

    $('.qp-zoomin-2').click(function() {
        if (ZOOM > 2) return
        dbg('+')
        dbg(MAIN_MESH.scaling)
        ZOOM += .1
        MAIN_MESH.scaling = new BABYLON.Vector3(ZOOM, ZOOM, -1*ZOOM)
    })
    $('.qp-zoomout-2').click(function() {
        if (ZOOM < .2) return
        dbg('-')
        ZOOM -= .1
        MAIN_MESH.scaling = new BABYLON.Vector3(ZOOM, ZOOM, -1*ZOOM)
    })
}

function handle_3d_3() {
    if (!BABYLON.Engine.isSupported()) {
        dbg("BABYLON is not Supported")
        return
    }
    var ZOOM = .1
    var ZOOM_STEP = .005
    var MAIN_MESH, CAP_MESH
    
    var canvas = document.getElementById("third-canvas");
    var engine = new BABYLON.Engine(canvas, true);
    var scene = new BABYLON.Scene(engine);
    // set scene background transparent
    scene.clearColor = new BABYLON.Color4(1,0,0,0);
    
    var light = new BABYLON.DirectionalLight("light1", new BABYLON.Vector3(4, -3, 0), scene);
    light.intensity = 3;
    var light2 = new BABYLON.HemisphericLight("light2", new BABYLON.Vector3(0, 1, 0), scene);
    light2.intensity = 0.7;
    
    var camera = new BABYLON.FreeCamera('camera', new BABYLON.Vector3(-4, 2, 0), scene);
    camera.setTarget(BABYLON.Vector3.Zero());
    camera.attachControl(canvas, false);
    
    BABYLON.SceneLoader.ImportMesh(["cap", "base"], "/static/quatropack2/models/", "bottle.gltf", scene,         
        function (meshes, particleSystems, skeletons) {
            //MAIN_MESH = meshes[0].children[0]
            //CAP_MESH = meshes[0].children[1]
            MAIN_MESH = meshes[0]
            CAP_MESH = meshes[1]
            //MAIN_MESH.setEnabled(false)
            //MAIN_MESH.visibility = 0
            //MAIN_MESH.isVisible = false
            MAIN_MESH.scaling = new BABYLON.Vector3(ZOOM, ZOOM, ZOOM)            
            CAP_MESH.scaling = new BABYLON.Vector3(ZOOM, ZOOM, ZOOM)
            dbg(ZOOM)
            dbg(MAIN_MESH)
            dbg(CAP_MESH)
            dbg(MAIN_MESH.position)
            dbg(CAP_MESH.position)
            MAIN_MESH.position = new BABYLON.Vector3(0, -1.5, 0)
            CAP_MESH.position = new BABYLON.Vector3(0, 15, 0)
            engine.runRenderLoop(function() {
                scene.render();
                MAIN_MESH.rotation.y -= 0.008
                //MAIN_MESH.position.y += 0.1
            });
            window.addEventListener("resize", function() {
                engine.resize();
            });
        });

    $('.qp-zoomin-3').click(function() {
        if (ZOOM > 3) return
        dbg('+')
        ZOOM += ZOOM_STEP
        MAIN_MESH.scaling = new BABYLON.Vector3(ZOOM, ZOOM, 1*ZOOM)
        CAP_MESH.scaling = new BABYLON.Vector3(ZOOM, ZOOM, 1*ZOOM)
        dbg(MAIN_MESH.scaling)
        dbg(CAP_MESH.scaling)
        dbg(ZOOM)
        dbg(MAIN_MESH.position)
        dbg(CAP_MESH.position)
    })
    $('.qp-zoomout-3').click(function() {
        if (ZOOM < .0001) return
        dbg('-')
        ZOOM -= ZOOM_STEP
        MAIN_MESH.scaling = new BABYLON.Vector3(ZOOM, ZOOM, 1*ZOOM)
        CAP_MESH.scaling = new BABYLON.Vector3(ZOOM, ZOOM, 1*ZOOM)
        dbg(MAIN_MESH.scaling)
        dbg(CAP_MESH.scaling)
        dbg(ZOOM)
        dbg(MAIN_MESH.position)
        dbg(CAP_MESH.position)
    })
}

$(function () {
    handle_3d()
    handle_3d_2()
    handle_3d_3()
})