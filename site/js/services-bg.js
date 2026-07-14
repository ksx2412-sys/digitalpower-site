import * as THREE from 'https://unpkg.com/three@0.160.0/build/three.module.js';

const container = document.getElementById('servicesBg');
if (container) {
  const NODE_COUNT = 220;
  const RADIUS = 4;
  const LINK_DIST = 1.15;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(50, 1, 0.1, 100);
  camera.position.z = 9;

  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  container.appendChild(renderer.domElement);

  // Fibonacci sphere distribution — even spread of "neurons"
  const positions = [];
  const golden = Math.PI * (3 - Math.sqrt(5));
  for (let i = 0; i < NODE_COUNT; i++) {
    const y = 1 - (i / (NODE_COUNT - 1)) * 2;
    const radiusAtY = Math.sqrt(1 - y * y);
    const theta = golden * i;
    positions.push(Math.cos(theta) * radiusAtY * RADIUS, y * RADIUS, Math.sin(theta) * radiusAtY * RADIUS);
  }

  const nodeGeometry = new THREE.BufferGeometry();
  nodeGeometry.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
  const nodeMaterial = new THREE.PointsMaterial({
    color: 0x8fb4ff,
    size: 0.085,
    transparent: true,
    opacity: 0.9,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
  });

  const linePositions = [];
  for (let i = 0; i < NODE_COUNT; i++) {
    for (let j = i + 1; j < NODE_COUNT; j++) {
      const dx = positions[i * 3] - positions[j * 3];
      const dy = positions[i * 3 + 1] - positions[j * 3 + 1];
      const dz = positions[i * 3 + 2] - positions[j * 3 + 2];
      if (Math.sqrt(dx * dx + dy * dy + dz * dz) < LINK_DIST) {
        linePositions.push(positions[i * 3], positions[i * 3 + 1], positions[i * 3 + 2]);
        linePositions.push(positions[j * 3], positions[j * 3 + 1], positions[j * 3 + 2]);
      }
    }
  }
  const lineGeometry = new THREE.BufferGeometry();
  lineGeometry.setAttribute('position', new THREE.Float32BufferAttribute(linePositions, 3));
  const lineMaterial = new THREE.LineBasicMaterial({ color: 0x2d6df0, transparent: true, opacity: 0.22 });

  const group = new THREE.Group();
  group.add(new THREE.Points(nodeGeometry, nodeMaterial));
  group.add(new THREE.LineSegments(lineGeometry, lineMaterial));
  scene.add(group);

  function resize() {
    const w = container.clientWidth || 1;
    const h = container.clientHeight || 1;
    renderer.setSize(w, h);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  }
  resize();
  window.addEventListener('resize', resize);

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  let rafId = null;
  function animate() {
    group.rotation.y += 0.0018;
    group.rotation.x = Math.sin(Date.now() * 0.0002) * 0.15;
    renderer.render(scene, camera);
    rafId = requestAnimationFrame(animate);
  }

  if (prefersReducedMotion) {
    renderer.render(scene, camera);
  } else {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          if (rafId === null) animate();
        } else if (rafId !== null) {
          cancelAnimationFrame(rafId);
          rafId = null;
        }
      });
    }, { threshold: 0.05 });
    observer.observe(container);
  }
}
